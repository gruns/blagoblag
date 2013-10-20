
Building a simple identity map in Django
========================================

:tags: django, models, orm

In Django's ticket tracker lies `ticket 17 <http://code.djangoproject.com/ticket/17>`_, the second oldest open ticket, this proposes an optimisation to have instances of the same database object be represented by the same object in Python, essentially that means for this code:

.. sourcecode:: python
    
    a = Model.objects.get(pk=3)
    b = Model.objects.get(pk=3)

a and b would be the same object at the memory level.  This can represent a large optimisation in memory usage if you're application has the potential to have duplicate objects(for example, related objects).  It is possible to implement a very simple identity map without touching the Django source at all.

The first step is to set up some very basic infastructure, this is going to be almost identical to what Eric Florenzano does in his post, `"Drop-dead simple Django caching" <http://www.eflorenzano.com/blog/post/drop-dead-simple-django-caching/>`_.

We start with a few helper functions:

.. sourcecode:: python
    
    _CACHE = {}
    
    def key_for_instance(obj, pk=None):
        if pk is None:
            pk = obj.pk
        return "%s-%s-%s" % (obj._meta.app_label, obj._meta.module_name, pk)
    
    def get_from_cache(klass, pk):
        return _CACHE[key_for_instance(klass, pk)]
    
    def cache_instance(instance):
        _CACHE[key_for_instance(instance)] = instance

We create our cache, which is a Python dictionary, a function to generate the cache key for an object, a function to get an item from the cache, and a function to cache an item.  How these work should be pretty simple.  Next we need to create some functions to make sure objects get update in the cache.

.. sourcecode:: python
    
    from django.db.models.signals import post_save, pre_delete
    
    def post_save_cache(sender, instance, **kwargs):
        cache_instance(instance)
    post_save.connect(post_save_cache)
    
    def pre_delete_uncache(sender, instance, **kwargs):
        try:
            del _CACHE[key_for_instance(instance)]
        except KeyError:
            pass
    pre_delete.connect(pre_delete_uncache)

Here we set up two signal receivers, when an object is saved we cache it, and when one is deleted we remove it from the cache.

Now we want a way to use our cache the way we already use our connection to the database, this means implementing some sort of hook in a QuerySet, this looks like:

.. sourcecode:: python
    
    from django.db.models.query import QuerySet
    
    class CachingQueryset(QuerySet):
        def __iter__(self):
            obj = self.values_list('pk', flat=True)
            for pk in obj:
                try:
                    yield get_from_cache(self.model, pk)
                except KeyError:
                    instance = QuerySet(self.model).get(pk=pk)
                    cache_instance(instance)
                    yield instance
    
        def get(self, *args, **kwargs):
            clone = self.filter(*args, **kwargs)
            objs = list(clone[:2])
            if len(objs) == 1:
                return objs[0]
            if not objs:
                raise self.model.DoesNotExist("%s matching query does not exist."
                                 % self.model._meta.object_name)
            raise self.model.MultipleObjectsReturned("get() returned more than one %s -- it returned %s! Lookup parameters were %s"
                    % (self.model._meta.object_name, len(objs), kwargs))
    

We create a subclass of QuerySet and override it's __iter__() and get() methods.  By default __iter__ does a fair bit of heavy lifting to internally cache the results and allow the usage of multiple iterators properly.  We override this to do something simpler.  We get the primary keys of each item in the queryset and iterate over them, if the object is in the cache we return it, otherwise we execute a database query to get it, and then cache it.  We also override get() to make sure it makes use of the caching we just set up.

To use this on a model we need to create a simple manager:

.. sourcecode:: python
    
    class CachingManager(Manager):
        def get_query_set(self):
            return CachingQuerySet(self.model)

And then we can use this with our models:

.. sourcecode:: python
    
    class Post(models.Model):
        title = models.CharField(max_length=100)
    
        objects = CachingManager()
    
    Post.objects.all()

Now all Posts accessed within the same thread will be cached using the strategy we've implemented.

This strategy will not save us database queries, indeed in some cases it can result in many more queries, it is designed to save memory usage(and be implemented as simply as possible).  It can also be made far more useful by having related objects use this strategy as well(if Post had a foreign key to author it would be nice to have all post authors share the same instances, since even you have a large queryset of Posts were all the Posts are unique, they are likely to have duplicate authors).

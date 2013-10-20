
Fixing up our identity mapper
=============================


The past two days we've been looking at building an identity mapper in Django.  Today we're going to implement some of the improvements I mentioned yesterday.

The first improvement we're going to do is it have it execute the query as usual and just cache the results, to prevent needing to execute additional queries.  This means changing the __iter__ method on our queryset class:

.. sourcecode:: python
    
        def __iter__(self):
            for obj in self.iterator():
                try:
                    yield get_from_cache(self.model, obj.pk)
                except KeyError:
                    cache_instance(obj)
                    yield obj

Now we just iterate over self.iterator() which is a slightly lower level interface to a querysets iteration, it bypasses all the caching that occurs(this means that for now at least, if we iterate over our queryset twice we actually execute two queries, whereas Django would normally do just one), however overall this will be a big win, since before if an item wasn't in the cache we would do an extra query for it.

The next improvement I proposed was to use Django's built in caching interfaces.  However, this won't work, this is because the built in locmem cache backend pickles and unpickles everything before caching and retrieving everything from the cache, so we'd end up with different objects(which defeats the point of this).

The last improvement we can make is to have this work on related objects for which we already know the primary key.  The obvious route to do this is to start hacking in django.db.models.fields.related, however as I've mentioned in a previous post this area of the code is a bit complex, however if we know a little bit about how this query is executed we can do the optimisation in a far simpler way.  As it turns out the related object descriptor simply tries to do the query using the default manager's get method.  Therefore, we can simply special case this occurrence in order to optimise this.  We also have to make a slight chance to our manager, as by default the manager won't be used on related object queries:

.. sourcecode:: python
    
    class CachingManager(Manager):
        use_for_related_fields = True
        def get_query_set(self):
            return CachingQuerySet(self.model)
    
    class CachingQueryset(QuerySet):
        ...
        def get(self, *args, **kwargs):
            if len(kwargs) == 1:
                k = kwargs.keys()[0]
                if k in ('pk', 'pk__exact', '%s' % self.model._meta.pk.attname, '%s__exact' % self.model._meta.pk.attname):
                    try:
                        return get_from_cache(self.model, kwargs[k])
                    except KeyError:
                        pass
            clone = self.filter(*args, **kwargs)
            objs = list(clone[:2])
            if len(objs) == 1:
                return objs[0]
            if not objs:
                raise self.model.DoesNotExist("%s matching query does not exist."
                                 % self.model._meta.object_name)
            raise self.model.MultipleObjectsReturned("get() returned more than one %s -- it returned %s! Lookup parameters were %s"
                    % (self.model._meta.object_name, len(objs), kwargs))

As you can see we just add one line to the manager, and a few lines to the begging of the get() method.  Basically our logic is if there is only one kwarg to the get() method, and it is a query on the primary key of the model, we try to return our cached instance.  Otherwise we fall back to executing the query.

And with this we've improved the efficiency of our identity map, there are almost definitely more places for optimisations, but now we have an identity map in very few lines of code.

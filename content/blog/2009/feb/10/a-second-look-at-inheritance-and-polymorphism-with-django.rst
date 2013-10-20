
A Second Look at Inheritance and Polymorphism with Django
=========================================================

:tags: django, internals, metaclass, models, orm, python

Previously I wrote about ways to handle polymorphism with inheritance in Django's ORM in a way that didn't require any changes to your model at all(besides adding in a mixin), today we're going to look at a way to do this that is a little more invasive and involved, but also can provide much better performance.  As we saw previously with no other information we could get the correct subclass for a given object in O(k) queries, where k is the number of subclasses.  This means for a queryset with n items, we would need to do O(nk) queries, not great performance, for a queryset with 10 items, and 3 subclasses we'd need to do 30 queries, which isn't really acceptable for most websites.  The major problem here is that for each object we simply guess as to which subclass a given object is.  However, that's a piece of information we could know concretely if we cached it for later usage, so let's start off there, we're going to be building a mixin class just like we did last time:

.. sourcecode:: python
    
    from django.db import models
    
    class InheritanceMixIn(models.Model):
        _class = models.CharField(max_length=100)
    
        class Meta:
            abstract = True
    

So now we have a simple abstract model that the base of our inheritance trees can subclass that has a field for caching which subclass we are.  Now let's add a method to actually cache it and retrieve the subclass:

.. sourcecode:: python
    
    from django.db import models
    from django.db.models.fields import FieldDoesNotExist
    from django.db.models.related import RelatedObject
    
    class InheritanceMixIn(models.Model):
        ...
        def save(self, *args, **kwargs):
            if not self.id:
                parent = self._meta.parents.keys()[0]
                subclasses = parent._meta.get_all_related_objects()
                for klass in subclasses:
                    if isinstance(klass, RelatedObject) and klass.field.primary_key \
                        and klass.opts == self._meta:
                        self._class = klass.get_accessor_name()
                        break
            return super(InheritanceMixIn, self).save(*args, **kwargs)
    
        def get_object(self):
            try:
                if self._class and self._meta.get_field_by_name(self._class)[0].opts != self._meta:
                    return getattr(self, self._class)
            except FieldDoesNotExist:
                pass
            return self

Our save method is where all the magic really happens.  First, we make sure we're only doing this caching if it's the first time a model is being saved.  Then we get the first parent class we have (this means this probably won't play nicely with multiple inheritance, that's unfortunate, but not as common a usecase), then we get all the related objects this class has(this includes the reverse relationship the subclasses have).  Then for each of the subclasses, if it is a RelatedObject, and it is a primary key on it's model, and the class it points to is the same as us then we cache the accessor name on the model, break out, and do the normal save procedure.

Our get_object function is pretty simple, if we have our class cached, and the model we are cached as isn't of the same type as ourselves we get the attribute with the subclass and return it, otherwise we are the last descendent and just return ourselves.  There is one(possible quite large) caveat here, if our inheritance chain is more than one level deep(that is to say our subclasses have subclasses) then this won't return those objects correctly.  The class is actually cached correctly, but since the top level object doesn't have an attribute by the name of the 2nd level subclass it doesn't return anything.  I believe this can be worked around, but I haven't found a way yet.  One idea would be to actually store the full ancestor chain in the CharField, comma separated, and then just traverse it.

There is one thing we can do to make this even easier, which is to have instances automatically become the correct subclass when they are pulled in from the DB.  This does have an overhead, pulling in a queryset with n items guarantees O(n) queries.  This can be improved(just as it was for the previous solution) by `ticket #7270 <http://code.djangoproject.com/ticket/7270>`_ which allows select_related to traverse reverse relationships.  In any event, we can write a metaclass to handle this for us automatically:

.. sourcecode:: python
    
    from django.db import models
    from django.db.models.base import ModelBase
    from django.db.models.fields import FieldDoesNotExist
    from django.db.models.related import RelatedObject
    
    class InheritanceMetaclass(ModelBase):
        def __call__(cls, *args, **kwargs):
            obj = super(InheritanceMetaclass, cls).__call__(*args, **kwargs)
            return obj.get_object()
    
    class InheritanceMixIn(models.Model):
        __metaclass__ = InheritanceMetaclass
        ...

Here we've created a fairly trivial metaclass that subclasses the default one Django uses for it's models.  The only method we've written is __call__, on a metalcass what __call__ does is handle the instantiation of an object, so it would call __init__.  What we do is do whatever the default __call__ does, so that we get an instances as normal, and then we call the get_object() method we wrote earlier and return it, and that's all.

We've now looked at 2 ways to handle polymorphism, with this way being more efficient in all cases(ignoring the overhead of having the extra charfield).  However, it still isn't totally efficient, and it fails in several edge cases.  Whether automating the handling of something like this is a good idea is something that needs to be considered on a project by project basis, as the extra queries can be a large overhead, however, they may not be avoidable in which case automating it is probably advantages.

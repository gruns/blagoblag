
Playing with Polymorphism in Django
===================================


One of the most common requests of people using inheritance in Django, is to have the a queryset from the baseclass return instances of the derives model, instead of those of the baseclass, as you might see with polymorphism in other languages.  This is a leaky abstraction of the fact that our Python classes are actually representing rows in separate tables in a database.  Django itself doesn't do this, because it would require expensive joins across all derived tables, which the user probably doesn't want in all situations.  For now, however, we can create a function that given an instance of the baseclass returns an instance of the appropriate subclass, be aware that this will preform up to k queries, where k is the number of subclasses we have.

First let's set up some test models to work with:

.. sourcecode:: python
    
    from django.db import models
    
    class Place(models.Model):
        name = models.CharField(max_length=50)
    
        def __unicode__(self):
            return u"%s the place" % self.name
    
    
    class Restaurant(Place):
        serves_pizza = models.BooleanField()
    
        def __unicode__(self):
            return "%s the restaurant" % self.name
    
    class Bar(Place):
        serves_wings = models.BooleanField()
    
        def __unicode__(self):
            return "%s the bar" % self.name
    

These are some fairly simple models that represents a common inheritance pattern.  Now what we want to do is be able to get an instance of the correct subclass for a given instance of Place.  To do this we'll create a mixin class, so that we can use this with other classes.

.. sourcecode:: python
    
    class InheritanceMixIn(object):
        def get_object(self):
            ...
    
    class Place(models.Model, InheritanceMixIn):
        ...

So what do we need to do in our get_object method?  Basically we need to loop each of the subclasses, try to get the correct attribute and return it if it's there, if none of them are there, we should just return ourself.  We start by looping over the fields:

.. sourcecode:: python
    
    class InheritanceMixIn(object):
        def get_object(self):
            for f in self._meta.get_all_field_names():
                field = self._meta.get_field_by_name(f)[0]

_meta is where Django stores lots of the internal data about a mode, so we get all of the field names, this includes the names of the reverse descriptors that related models provide.  Then we get the actual field for each of these names.  Now that we have each of the fields we need to test if it's one of the reverse descriptors for the subclasses:

.. sourcecode:: python
    
    from django.db.models.related import RelatedObject
    
    class InheritanceMixIn(object):
        def get_object(self):
            for f in self._meta.get_all_field_names():
                field = self._meta.get_field_by_name(f)[0]
                if isinstance(field, RelatedObject) and field.field.primary_key:

We first test if the field is a RelatedObject, and if it we see if the field on the other model is a primary key, which it will be if it's a subclass(or technically any one to one that is a primary key).  Lastly we need to find what the name of that attribute is on our model and to try to return it:

.. sourcecode:: python
    
    class InheritanceMixIn(object):
        def get_object(self):
            for f in self._meta.get_all_field_names():
                field = self._meta.get_field_by_name(f)[0]
                if isinstance(field, RelatedObject) and field.field.primary_key:
                    try:
                        return getattr(self, field.get_accessor_name())
                    except field.model.DoesNotExist:
                        pass
            return self

We try to return the attribute, and if it raises a DoesNotExist exception we move on to the next one, if none of them return anything, we just return ourself.

And that's all it takes.  This won't be super efficient, since for a queryset of n objects, this will take O(n*k) given k subclasses.  `Ticket 7270 <http://code.djangoproject.com/ticket/7270>`_ deals with allowing select_related() to work across reverse one to one relations as well, which will allow one to optimise this, since the subclasses would already be gotten from the database.

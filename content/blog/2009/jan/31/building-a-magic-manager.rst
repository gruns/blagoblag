
Building a Magic Manager
========================

:tags: django, models, orm, python

A very common pattern in Django is to create methods on a manager to abstract some usage of ones data.  Some people take a second step and actually create a custom QuerySet subclass with these methods and have their manager proxy these methods to the QuerySet, this pattern is seen in Eric Florenzano's `Django From the Ground Up <http://thisweekindjango.com/screencasts/episode/11/django-ground-episode-3/>`_ screencast.  However, this requires a lot of repetition, it would be far less verbose if we could just define our methods once and have them available to us on both our managers and QuerySets.

Django's manager class has one hook for providing the QuerySet, so we'll start with this:

.. sourcecode:: python
    
    from django.db import models
    
    class MagicManager(models.Manager):
       def get_query_set(self):
           qs = super(MagicManager, self).get_query_set()
           return qs

Here we have a very simple get_query_set method, it doesn't do anything but return it's parent's queryset.  Now we need to actually get the methods defined on our class onto the queryset:


.. sourcecode:: python
    
    class MagicManager(models.Manager):
       def get_query_set(self):
           qs = super(MagicManager, self).get_query_set()
           class _QuerySet(qs.__class__):
               pass
           for method in [attr for attr in dir(self) if not attr.startswith('__') and callable(getattr(self, attr)) and not hasattr(_QuerySet, attr)]:
               setattr(_QuerySet, method, getattr(self, method))
           qs.__class__ = _QuerySet
           return qs

The trick here is we dynamically create a subclass of whatever class the call to our parent's get_query_set method returns, then we take each attribute on ourself, and if the queryset doesn't have an attribute by that name, and if that attribute is a method then we assign it to our QuerySet subclass.  Finally we set the __class__ attribute of the queryset to be our QuerySet subclass.  The reason this works is when Django chains queryset methods it makes the copy of the queryset have the same class as the current one, so anything we add to our manager will not only be available on the immediately following queryset, but on any that follow due to chaining.

Now that we have this we can simply subclass it to add methods, and then add it to our models like a regular manager.  Whether this is a good idea is a debatable issue, on the one hand having to write methods twice is a gross violation of Don't Repeat Yourself, however this is exceptionally implicit, which is a major violation of The Zen of Python.

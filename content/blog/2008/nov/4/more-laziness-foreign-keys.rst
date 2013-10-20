
More Laziness with Foreign Keys
===============================

:tags: django, foreignkey, models, orm

Yesterday we looked at building a form field to make the process of getting a ForeignKey to the User model more simple, and to provide us with some useful tools, like the manager.  But this process can be generalized, and made more robust.  First we want to have a lazy ForeignKey field for all models(be careful not to confuse the term lazy, here I use it to refer to the fact that I am a lazy person, not the fact that foreign keys are lazy loaded).

A more generic lazy foreign key field might look like:

.. sourcecode:: python

   from django.db.models import ForeignKey, Manager

   class LazyForeignKey(ForeignKey):
       def __init__(self, *args, **kwargs):
           model = kwargs.get('to')
           if model_name is None:
               model = args[0]
           try:
               name = model._meta.object_name.lower()
           except AttributeError:
               name = model.split('.')[-1].lower()
           self.manager_name = kwargs.pop('manager_name', 'for_%s' % name)
           super(ForeignKey, self).__init__(*args, **kwargs)
     
       def contribute_to_class(self, cls, name):
           super(ForeignKey, self).contribute_to_class(cls, name)
         
           class MyManager(Manager):
               def __call__(self2, obj):
                   return cls._default_manager.filter(**{self.name: obj})
         
           cls.add_to_class(self.manager_name, MyManager())

As you can see, a lot of the code is the same as before.  Most of the new code is in getting the mode's name, either through _meta, or through the last part of the string(i.e. User in "auth.User").  And now you will have a manager on your class, named either for_X where X is the name of the model the foreign key is to lowercase, or named whatever the kwarg manager_name is.

So if your model has this:

.. sourcecode:: python

   teacher = LazyForeignKey(Teacher)

You would be able to do:

.. sourcecode:: python

   MyModel.for_teacher(Teacher.objects.get(id=3))


That's all for today.  Since tonight is election night, tomorrow I'll probably post about my application election-sim, and about PyGTK and PyProcessing(aka multiprocessing).

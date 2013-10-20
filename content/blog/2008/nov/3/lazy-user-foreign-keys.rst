
Lazy User Foreign Keys
======================

:tags: django, foreignkey, models, orm

A *very* common pattern in Django is for models to have a foreign key to django.contrib.auth.User for the owner(or submitter, or whatever other relation with User) and then to have views that filter this down to the related objects for a specific user(often the currently logged in user).  If we think ahead, we can make a manager with a method to filter down to a specific user.  But since we are really lazy we are going to make a field that automatically generates the foreign key to User, and gives us a manager, automatically, to filter for a specific User, and we can reuse this for all types of models.

So what does the code look like:

.. sourcecode:: python
    
   from django.db.models import ForeignKey, Manager

   from django.contrib.auth.models import User

   class LazyUserForeignKey(ForeignKey):
       def __init__(self, **kwargs):
           kwargs['to'] = User
           self.manager_name = kwargs.pop('manager_name', 'for_user')
           super(ForeignKey, self).__init__(**kwargs)
     
       def contribute_to_class(self, cls, name):
           super(ForeignKey, self).contribute_to_class(cls, name)
         
           class MyManager(Manager):
               def __call__(self2, user):
                   return cls._default_manager.filter(**{self.name: user})
         
           cls.add_to_class(self.manager_name, MyManager())

So now, what does this do?

We are subclassing ForeignKey.  In __init__ we make sure to is set to User and we also set self.manager_name equal to either the manager_name kwarg, if provided or 'for_user'.  contribute_to_class get called by the ModelMetaclass to add each item to the Model itself.  So here we call the parent method, to get the ForeignKey itself set on the model, and then we create a new subclass of Manager.  And we define an __call__ method on it, this lets us call an instance as if it were a function.  And we make __call__ return the QuerySet that would be returned by filtering the default manager for the class where the user field is equal to the given user.  And then we add it to the class with the name provided earlier.

And that's all.  Now we can do things like:

.. sourcecode:: python

   MyModel.for_user(request.user)

Next post we'll probably look at making this more generic.

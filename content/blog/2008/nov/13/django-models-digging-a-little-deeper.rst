
Django Models - Digging a Little Deeper
=======================================


For those of you who read my last post on Django models you probably noticed that I skirted over a few details, specifically for quite a few items I said we, "added them to the new class".  But what exactly does that entail?  Here I'm going to look at the add_to_class method that's present on the ModelBase metaclass we look at earlier, and the contribute_to_class method that's present on a number of classes throughout Django.

So first, the add_to_class method.  This is called for each item we add to the new class, and what it does is if that has a contribute_to_class method than we call that with the new class, and it's name(the name it should attach itself to the new class as) as arguments.  Otherwise we simply set that attribute to that value on the new class.  So for example new_class.add_to_class('abc', 3), 3 doesn't have a contribute_to_class method, so we just do setattr(new_class, 'abc', 3).

The contribute_to_class method is more common for things you set on your class, like Fields or Managers.  The contribute_to_class method on these objects is responsible for doing whatever is necessary to add it to the new class and do it's setup.  If you remember from my first blog post about User Foreign Keys, we used the contribute_to_class method to add a new manager to our class.  Here we're going to look at what a few of the builtin contribute_to_class methods do.

The first case is a manager.  The manager sets it's model attribute to be the model it's added to.  Then it checks to see whether or not the model already has an _default_manager attribute, if it doesn't, or if it's creation counter is lower than that of the current creation counter, it sets itself as the default manager on the new class.  The creation counter is essentially a way for Django to keep track of which manager was added to the model first.  Lastly, if this is an abstract model, it adds itself to the abstract_managers list in _meta on the model.

The next case is if the object is a field, different fields actually do slightly different things, but first we'll cover the general field case.  It also, first, sets a few of it's internal attributes, to know what it's name is on the new model, additionally calculating it's column name in the db, and it's verbose_name if one isn't explicitly provided.  Next it calls add_field on _meta of the model to add itself to _meta.  Lastly, if the field has choices, it sets the get_FIELD_display method on the class.

Another case is for file fields.  They do everything a normal field does, plus some more stuff.  They also add a FileDescriptor to the new class, and they also add a signal receiver so that when an instance of the model is deleted the file also gets deleted.

The final case is for related fields.  This is also the most complicated case.  I won't describe exactly what this code does, but it's biggest responsibility is to set up the reverse descriptors on the related model, those are nice things that let you author_obj.books.all().

Hopefully this gives you a good idea of what to do if you wanted to create a new field like object in Django.  For another example of using these techniques, take a look at the generic foreign key field in django.contrib.contenttypes, `here <http://code.djangoproject.com/browser/django/trunk/django/contrib/contenttypes/generic.py#L16>`_.

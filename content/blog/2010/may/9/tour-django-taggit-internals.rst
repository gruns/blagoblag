
A Tour of the django-taggit Internals 
======================================


In `a previous post <http://alexgaynor.net/2010/may/04/cool-new-django-taggit-api/>`_ I talked about a cool new customization API that ``django-taggit`` has.  Now I'm going to dive into the internals.

The public API is almost exclusively exposed via a class named ``TaggableManager``, you attach one of these to your model and it has some cool tagging APIs.  This class basically masquerades as ``ManyToManyField``, this is how it gets cool things like filtering and forms automatically.  If you look at its definition you'll see it has a bunch of attributes that it never actually uses, basically all of these act to emulate the ``Field`` interface.  This class is also the entry point for the new customization API, exposed via the ``through`` parameter.  This basically acts as an analogue to the ``through`` parameter on actual ``ManyToManyFields`` (`documented here <http://docs.djangoproject.com/en/dev/topics/db/models/#intermediary-manytomany>`_).  The final crucial method is ``__get__``, which turns ``TaggableManager`` into a descriptor.

This descriptor exposes an ``_TaggableManager`` class, which holds some of the internal logic.  This class exposes all of the "managery" type methods, ``add()``, ``set()``, ``remove()``, and ``clear()``.  This class is pretty simple, basically it just proxies bewteen the methods called and it's ``through`` model.  This class is, unlike ``TaggableManager``, actually a subclass of ``models.Manager``, it just defines ``get_query_set()`` to return a ``QuerySet`` of all the tags for that model, or instance, and then filtering, ordering, and more falls out naturally.

Beyond that there's not too much going on.  The code is fairly simple, and it's not particularly long.  I've found this to be a pretty good pattern for extensibility, and it really resolves the need to have dozens of parameters, or ``GenericForeignKeys`` popping out every which way.

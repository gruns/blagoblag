
Towards Application Objects in Django 
======================================

:tags: applications, django, python, reusable

Django's application paradigm (and the accompanying reusable application environment) have served it exceptionally well, however there are a few well known problems with it.  Chief among these is pain in extendability (as exemplified by the ``User`` model), and abuse of ``GenericForeignKeys`` where a true ``ForeignKey`` would suffice (in the name of being generic), there are also smaller issues, such as wanting to install the same application multiple times, or having applications with the same "label" (in Django parlance this means the ``path.split(".")[-1]``).  Lately I've been thinking that the solution to these problems is a more holistic approach to application construction.

It's a little difficult to describe precisely what I'm thinking about, so I'll start with an example:

.. sourcecode:: python

    from django.contrib.auth import models as auth_models
    
    class AuthApplication(Application):
        models = auth_models

        def login(self, request, template_name='registration/login.html'):
            pass

        # ... etc


And in settings.py:

.. sourcecode:: python

    from django.core import app

    INSTALLED_APPS = [
        app("django.contrib.auth.AuthApplication", label="auth"),
    ]


The critical elements are that a) all models are referred to be the attribute on the class, so that they can be swapped out by a subclass, b) applications are now installed using an ``app`` object that wraps the app class, with a label (to allow multiple apps of the same name to be registered).  But how does this allow swapping out the ``User`` model, from the perspective of people who are expecting to just be able to use ``django.contrib.auth.models.User`` for any purpose?  Instead of explicit references to the model these could be replaced with: ``get_app("auth").models.User``.

What about the issue of ``GenericForeignKeys``?  To solve these we'd really need something like C++'s templates, or Java's generics, but we'll settle for the next best thing, callables!  Imagine a comment app where the ``models.py`` looked like:

.. sourcecode:: python

    from django.core import get_app
    from django.db import models
    
    def get_models(target_model):
        class Comment(models.Model):
            obj = models.ForeignKey(target_model)
            commenter = models.ForeignKey(get_app("auth").models.User)
            text = models.TextField()

        return [Comment]


Then instead of providing a module to be ``models`` on the application class this callable would be provided, and Django would know to call it with the appropriate model class based on either a class attribute (for subclasses) or a parameter from the ``app`` object (to allow for easily installing more than one of the comment app, for each object that should allow commenting), in practice I think allowing the same app to be installed multiple times would require some extra parameters to the ``get_models`` function, so that things like ``db_table`` can be adjusted appropriately.

I think this could be done in a backwards compatible manner, by having strings that are in ``INSTALLED_APPS`` automatically generate an ``app`` object that was the default "filler" one with just a ``models`` module, and the views ignoring ``self``, and a default label.  Like I said this is all just a set of ideas floating around my brain at this point, but hopefully by floating this design it'll get people thinking about big architecture ideas like this.

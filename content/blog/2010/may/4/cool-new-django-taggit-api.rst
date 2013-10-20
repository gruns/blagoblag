
Cool New django-taggit API
==========================

:tags: applications, django, python

A little while ago `I wrote <http://alexgaynor.net/2010/mar/28/towards-application-objects-django/>`_ about some of the issues with the reusable application paradigm in Django.  Yesterday `Carl Meyer <http://twitter.com/carljm>`_ pinged me about an issue in django-taggit, it uses an ``IntegerField`` for the ``GenericForeignKey``, which is great.  Except for when you have a model with a ``CharField``, ``TextField``, or anything else for a primary key.  The easy solution is to change the ``GenericForeignKey`` to be something else.  But that's lame, a pain in the ass, and a hack (more of a hack than a ``GenericForeignKey`` in the first place).

The alternate solution we came up with:

.. sourcecode:: python

    from django.db import models

    from taggit.managers import TaggableManager
    from taggit.models import TaggedItemBase


    class TaggedFood(TaggedItemBase):
        content_object = models.ForeignKey('Food')

    class Food(models.Model):
        # ... fields here

        tags = TaggableManager(through=TaggedFood)


Custom through models for the taggable relationship!  This let's the included ``GenericForeignKey`` implementation cater to the common case of integer primary keys, and lets other people provide their own implementations when necessary.  Plus it means doing things like, adding a ``ForeignKey`` to ``auth.User`` or adding the "originally" typed version of the tag (for systems where tags are normalized).

In addition I've finally added some docs, they aren't really complete, but they're a start.  I'm planning a release for sometime next week, unless some major issue pops up.

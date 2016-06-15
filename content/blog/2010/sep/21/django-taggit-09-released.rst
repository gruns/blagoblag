
django-taggit 0.9 Released
==========================


It's been a long time coming, since taggit 0.8 was released in June, however 0.9 is finally here, and it brings a ton of cool bug fixes, improvements, and cleanups.  If you don't already know, django-taggit is an application for django to make tagging simple and awesome.  The biggest changes in this release are:

 * The addition of a bunch of locales.
 * Support for custom tag models.
 * Moving ``taggit.contrib.suggest`` into an external package.
 * Changed the filter syntax from ``filter(tags__in=["foo"])`` to
   ``filter(tags__name__in=["foo"])``.  This change is backwards incompatible,
   but was necessary to support lookups on all fields.


You can checkout `the docs <https://django-taggit.readthedocs.io/>`_ for complete details.  The goals for the 1.0 release are going to be adding some useful widgets for use in the admin and forms, hopefully adding a class based generic view to replace the current one, and adding a migration command to move data from django-tagging into the django-taggit models.

You can get the `latest release on PyPi <http://pypi.python.org/pypi/django-taggit>`_.  Enjoy.

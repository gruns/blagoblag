
New Admin URLs
==============

:tags: django, internals

I'm very happy to announce that with `revision 9739 <http://code.djangoproject.com/changeset/9739>`_ of Django the admin now uses normal URL resolvers and its URLs can be reversed.  This is a tremendous improvement over the previous ad hoc system and it gives users the distinct advantage of being able to reverse the admin's URLs.  However, in order to make this work a new feature went into the URL resolving system that any user can use in their own code.

Specifically users can now have objects which provide URLs.  Basically this is because include() can now accept any iterable, rather than just a string which points to a urlconf.  To get an idea of what this looks like you can look at `the way the admin now does it <http://code.djangoproject.com/browser/django/trunk/django/contrib/admin/sites.py#L151>`_.

There are going to be a few more great additions to Django going in as we move towards the 1.1 alpha so keep an eye out for them.

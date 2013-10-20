
Doing a release is too hard
===========================

:tags: django, open-source, openstack, python

I just shipped a new release of `alchimia`_. Here are the steps I went through:

* Manually edit version numbers in ``setup.py`` and ``docs/conf.py``. In theory
  I could probably centralize this, but then I'd still have a place I need to
  update manually.
* Issue a ``git tag`` (actually I forgot to do that on this project, oops).
* ``python setup.py register sdist upload -s`` to build and upload some
  tarballs to PyPi
* ``python setup.py register bdist_wheel upload -s`` to build and upload some
  wheels to PyPi
* Bump the version again for the now pre-release status (I never remeber to do
  this)

Here's how it works for OpenStack projects:

* ``git tag VERSION -s`` (``-s``) makes it be a GPG signed tag)
* ``git push gerrit VERSION`` this sends the tag to gerrit for review

Once the tag is approved in the code review system, a release will
automatically be issue including:

* Uploading to PyPi
* Uploading documentation
* Landing the tag in the official repository

Version numbers are always automatically handled correctly.

This is how it should be. We need to bring this level of automation to all
projects.

.. _`alchimia`: http://alchimia.readthedocs.org/en/latest/

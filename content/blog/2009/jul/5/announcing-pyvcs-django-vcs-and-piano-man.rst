
Announcing pyvcs, django-vcs, and piano-man
===========================================

:tags: django, python, release, vcs

`Justin Lilly <http://www.justinlilly.com/>`_ and I have just released pyvcs, a lightweight abstraction layer on top of multiple version control systems, and django-vcs, a Django application leveraging pyvcs in order to provide a web interface to version control systems.  At this point pyvcs exists exclusively to serve the needs of django-vcs, although it is separate and completely usable on its own.  Django-vcs has a robust feature set, including listing recent commits, pretty diff rendering of commits, and code browsing.  It also supports multiple projects.  Both pyvcs and django-vcs currently support Git and Mercurial, although adding support for a new backend is as simple as implementing four methods and we'd love to be able to support additional VCS like Subversion or Bazaar.  Django-vcs comes with some starter templates (as well as CSS to support the pretty diff rendering).

It goes without saying that we'd like to thank the authors of the VCS themselves, in addition we'd like to thank the authors of Dulwich, for providing a pure Python implementation of the Git protocol, as well as the Pocoo guys, for pygments, the syntax highlighting library for Python, as well as the pretty diff rendering which we lifted out of the lodgeit pastbin application.

Having announced what we have already, we'll now be looking towards the future.  As such Justin and I plan to be starting a new Django project "piano-man".  Piano-man, a reference to Billy Joel, follows the Django tradition of naming things after musicians (although we've branched out a bit, leaving the realm of Jazz in favour of Rock 'n Roll).  Piano-man will be a complete web based project management system, similar to Trac or Redmine.  There are a number of logistical details that we still need to sort out, such as whether this will be a part of Pinax as a "code edition" or whether it will be a separate project entirely, like Satchmo and Reviewboard.

Some people are inevitably asking why we've chosen to start a new project, instead of working to improve one of the existing ones I alluded to.  The reason is, after hearing coworkers complain about poor Git support in Trac (even with external plugins), and friends complain about the need to modify Redmine just to support branches in Git properly I'd become convinced it couldn't possibly be that hard, and I think Justin and I have proven that it isn't.  All the work you see in pyvcs and django-vcs took 48 hours to complete, with both of us working evenings and a little bit during the day on these projects.

You can find both django-vcs and pyvcs on PyPi as well on Github under my account (http://github.com/alex/), both are released under the BSD license.  We hope you enjoy both these projects and find them helpful, and we'd appreciate and contributions, just file bugs on Github.  I'll have another blog post in a few days outlining the plan for piano-man once Justin and I work out the logistics.  Enjoy.

Edit:  I seem to have forgotten all the relevant links, here they are

 * `pyvcs on github <https://github.com/alex/pyvcs>`_
 * `django-vcs on github <http://github.com/alex/django-vcs/>`_
 * `piano-man on github <http://github.com/alex/piano-man>`_
 * `pyvcs on PyPi <http://pypi.python.org/pypi/pyvcs>`_
 * `django-vcs on PyPi <http://pypi.python.org/pypi/django-vcs>`_

Sorry about that.

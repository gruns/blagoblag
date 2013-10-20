
My Workflow
===========

:tags: easy_install, pip, python, virtualenv, virtualenvwrapper

About a year ago I blogged about how I didn't like easy_install, and I alluded to the fact that I didn't really like any programming language specific package managers.  I'm happy to say I've changed my tune quite drastically in the past 2 months.  Since I started working with Eldarion I've dived head first into the `pip <http://pip.openplans.org/>`_ and `virtualenv <http://pypi.python.org/pypi/virtualenv>`_ system and I'm happy to say it works brilliantly.  The nature of the work is that we have lots of different projects all at once, often using wildly different versions of packages in all sorts of incompatible ways.  The only way to stay sane is to have isolated environments for each of them.  Enter virtualenv stage left.

If you work with multiple Python projects that use different versions of things virtualenv is indispensable.  It allows you to have totally isolated execution environments for different projects.  I'm also using `Doug Hellmann's <http://www.doughellmann.com/>`_ `virtualenvwrapper <http://www.doughellmann.com/projects/virtualenvwrapper/>`_, which wraps up a few virtualenv commands and gives you some hooks you can use.  When I start a new project it looks something like this:

.. sourcecode:: bash
    
        $ git checkout some_repo
        $ cd some_repo/
        $ mkvirtualenv project_name

The first two steps are probably self explanatory.  What mkvirtualenv does is to a new virtual environment, and activate it.  I also have a hook set up with virtualenvwrapper to install the latest development version of pip, as well as ipython and ipdb.  pip is a tremendous asset to this process.  It has a requirements file that makes it very easy to keep track of all the dependencies for a given project, plus pip allows you to install packages out of a version control system which is tremendously useful.

When I want to work on an existing project all I need to do is:

.. sourcecode:: bash
    
        $ workon project_name

This activates the environment for that project.  Now the PATH prioritizes stuff installed into that virtualenv, and my Python path only has stuff installed into this virtualenv.  I can't imagine what my job would be like without these tools, if I had to manually manage the dependencies for each project I'd probably go crazy within a week.  Another advantage is it makes it easy to test things against multiple versions of a library.  I can test if something works on Django 1.0 and 1.1 just by switching which environment I'm in.

As promised tomorrow I'll be writing about an optimization that just landed in Unladen Swallow, and I'm keeping Monday's post a secret.  I'm not sure what Tuesday's post will be, but I think I'll be writing something Django related, either about my new templatetag library, or the state of my multiple database work.  See you around the internet.

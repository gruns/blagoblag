
Why I don't use easy_install
============================

:tags: easy_install, python, ubuntu

First things first, this post is not meant as a flame, nor should it indicate to you that you shouldn't use it, unless of course you're priorities are perfectly aligned with my own.  That being said, here are the reasons why I don't use easy_install, and how I'd fix them.
 * No easy_uninstall.  Zed mentioned this in his PyCon '08 lightning talk, and it's still true.  Yes I can simply remove these files, and yeah I could write a script to do it for me.  But I shouldn't have to, if I can install packages, I should be able to uninstall packages, without doing any work.
 * I can't update all of my currently installed packages.  For any packages I don't have explicitly installed to a particular version(which to it's credit, easy_install makes very easy to do), it should be very to upgrade all of these, because I probably want to have them up to date, and I can always lock them at a specific version if I want.
 * I don't want to have two package managers on my machine.  I run Ubuntu, so I already have apt-get, which i find to be a really good system(and doesn't suffer from either of the aforementioned problems).  Having two packages managers inherently brings additional confusion, if a package is available in both which do I install it from?  It's an extra thing to remember to keep up to date(assuming #2 is fixed), and it's, in general, an extra thing to think about, every time I go to update anything on my machine.

So what's my solution?  PyPi is a tremendous resource for Python libraries, and there are great tools in Python for working with it, for example using a setup.py file makes it incredibly easy to get your package up on PyPi, and keep it up to date.  So there's no reason to throw all that stuff out the window.  My solution would be for someone to set up a server that mirrored all the data from PyPi, regularly, and then offered the packages as .deb's(for Debian/Ubuntu users, and as RPMs for Fedora users, etc...).  That way all a user of a given package manager can just add the URL to their sources list, and then install everything that's available from PyPi, plus they derive all of the benefits of their given package manager(for me personally, the ability to uninstall and batch upgrade).

Note: I'm not suggesting everyone use apt-get, I'm merely suggesting everyone use their native package manager, and there's no reason easy_install/pip/virtualenv can't also be used.

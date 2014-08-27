Long Live curl(1)
=================

Ever looked at an installation guide that told you to do something like ``curl
-O https://... | sudo sh``?

Ever made fun of some software for such *obviously* ridiculous and terrible
installation instructions?

How about::

    $ sudo apt-key add '...'
    $ sudo add-apt-repository https://...
    $ sudo apt-get install '...'

Betcha didn't make fun of that one.

Why is that?

Why do people delight in mocking the ``curl | sudo sh`` instructions, but the
``apt-get`` ones are perfectly fine?

I suppose one reason is that many of the ``curl`` instructions point at
``http://`` URLs (no TLS), which leave the user open to trivial MITM attacks.

Fair enough, not using ``https`` on the internet today is exposing your users
to unnecessary risk.

But, nonetheless, folks who use ``https`` are still getting mocked. And the
reason seems to be security?

I care about security a great deal, so I want to dissect what the security
implications for each of these is.

curl
----

The author of the program has root access on your machine at installation time
and can do *whatever they please*. That's quite a bit of access, but it's
temporally constrained (if they don't do anything bad at install time, they
can't go back and do it later).

Of course, they'll also have whatever permissions you run the installed
software as, but that's a given.

apt-get
-------

The author of the program has root access on your machine at installation time
and can do *whatever they please* (to quote a friend of mine: "any deb can
completely replace your entire system, including the kernel").

Unlike with ``curl``, this access has no temporal constraints, even if the
original ``.deb`` wasn't malicious, the next time you ``sudo apt-get update &&
sudo apt-get ugprade`` the author can ship you a new piece of, potentially
malicious, software.

This means that a popular apt repository, if compromised, could go on to
compromise millions of other computers.

Conclusion
----------

As far as I can tell, an approach for software distribution that's predicated
on adding new apt repositories exposes users to greater potential security
risks than ``curl https:// | sudo sh``.

What's the alternative to this? Package managers and operating systems which
support installing software into its own sandbox. For a model of how this might
work, take a look at the iPhone, its package manager (The App Store) allows
users to install *anything* confident it will not be able to compromise their
system state.

PS: Running tons of random scripts to install things is probably a bad idea for
maintainability, but that is, as they say, another fox hunt altogether.

There is a flash of light! Your PYTHON has evolved into ...
===========================================================

This year has been marked, for me, by many many discussions of Python versions.
Finally, though, I've acquiesced, I've seen the light, and I'm doing what many
have suggested. I'm taking the first steps: I'm changing my default Python.

Yes indeed, my global ``python`` is now something different::

    $ python
    Python 2.7.6 (32f35069a16d, Jun 06 2014, 20:12:47)
    [PyPy 2.3.1 with GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.2.79)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>>

Yup, my default ``python`` is now `PyPy`_.

Why?

Because I believe PyPy is the future, and I want to stamp out every single
possible bug and annoyance a person might hit, and the best way to do that is
to subject myself to them constantly. If startup performance is too slow, you
know for damned sure I'll get pissed off and try to fix it.

But this shouldn't be just me! I'm only one day into this, but thus far: I've
found one bug in Mercurial's ``setup.py``, and lots of my random scripts run
faster. In today's revolution spirit, I want to encourage you too to cast off
the shackles of slow Python, and embrace the possibility of performance without
compromises!

If you run into any issues at all: packages that won't install, things that are
too slow, or take too much memory. You can email me personally. I'm committed
to making this the most fantastic Python experience you could ever have.

Technical details
-----------------

I changed by default Python, or OS X, using `pyenv`_::

    $ brew install pyenv
    $ # Muck with my fish config
    $ pyenv install pypy-2.3.1
    $ pyenv global pypy-2.3.1
    $ pip install a nice list of utilities I use

Tada.

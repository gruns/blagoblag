
So you want to write a fast Python? 
====================================

:tags: programming, pypy, python

Thinking about writing your own Python implementation? Congrats, there are
plenty out there [#]_, but perhaps you have something new to bring to the
table. Writing a fast Python is a pretty hard task, and there's a lot of stuff
you need to keep in mind, but if you're interested in forging ahead, keep
reading!

First, you'll need to write yourself an interpreter. A static compiler for
Python doesn't have enough information to do the right things [#]_ [#]_, and a
multi-stage JIT compiler is probably more trouble than it's worth [#]_. It
doesn't need to be super fast, but it should be within 2x of CPython or so, or
you'll have lost too much ground to make up later. You'll probably need to
write yourself a garbage collector as well, it should probably be a nice,
generational collector [#]_.

Next you'll need implementations for all the builtins. Be careful here! You
need to be every bit as good as CPython's algorithms if you want to stand a
chance, this means things like ``list.sort()`` keeping up with Timsort [#]_,
``str.__contains__`` keeping up with fast search [#]_, and ``dict.__getitem__``
keeping up with the extremely carefully optimized Python ``dict`` [#]_.

Now you've got the core language, take a bow, most people don't make it nearly
this far! However, there's still tons of work to go, for example you need the
standard library if you want people to actually use this thing. A lot of the
stdlib is in Python, so you can just copy that, but some stuff isn't, for that
you'll need to reimplement it yourself (you can "cheat" on a lot of stuff and
just write it in Python though, rather than C, or whatever language your
interpreter is written in).

At this point you should have yourself a complete Python that's basically a
drop-in replacement for CPython, but that's a bit slower. Now it's time for
the real work to begin. You need to write a Just in Time compiler, and it
needs to be a good one. You'll need a great optimizer that can simultaneously
understand some of the high level semantics of Python, as well as the low
level nitty gritty of your CPU [#]_.

If you've gotten this far, you deserve a round of applause, not many projects
make it this far. But your Python probably still isn't going to be used by the
world, you may execute Python code 10x faster, but the Python community is
more demanding than that. If you want people to really use this thing you're
going to have to make sure their C extensions run. Sure, CPython's C-API was
never designed to be run on other platforms, but you can make it work, even if
it's not super fast, it might be enough for some people [#]_.

Finally, remember that standard library you wrote earlier? Did you make sure
to take your time to optimize it? You're probably going to need to take a step
back and do that now, sure it's huge, and people use every nook and cranny of
it, but if you want to be faster, you need it to be faster too. It won't do
to have your ``bz2`` module be slower, tarnishing your beautiful speed
results [#]_.

Still with me? Congratulations, you're in a class of your own. You've got a
blazing fast Python, a nicely optimized standard library, and you can run
anyone's code, Python or C. If this ballad sounds a little familiar, that's
because it is, it's the story of PyPy. If you think this was a fun journey,
you can join in. There are ways for Python programmers at every level to help
us, such as:

* Contributing to our performance analysis tool, this is actually a web app
  written using ``Flask``.
* Contribute to `speed.pypy.org`_ which is a Django site.
* Provide pure Python versions of your C-extensions, to ensure they run on
  alternative Pythons.
* Test and benchmark your code on PyPy, let us know if you think we should be
  faster! (We're always interested in slower code, and we consider it a bug)
* Contribute to PyPy itself, we've got tons of things to do, you could work on
  the standard library, the JIT compiler, the GC, or anything in between.

Hope to see you soon [#]_!

.. _`speed.pypy.org`: http://speed.pypy.org/

.. [#] CPython, IronPython, Jython, PyPy, at least!
.. [#] http://code.google.com/p/shedskin/
.. [#] http://cython.org/
.. [#] http://code.google.com/p/v8/
.. [#] http://docs.python.org/c-api/refcounting.html
.. [#] http://hg.python.org/cpython/file/2.7/Objects/listsort.txt
.. [#] http://effbot.org/zone/stringlib.htm
.. [#] http://hg.python.org/cpython/file/2.7/Objects/dictnotes.txt
.. [#] http://code.google.com/p/unladen-swallow/
.. [#] http://code.google.com/p/ironclad/
.. [#] https://bugs.pypy.org/issue733
.. [#] http://pypy.org/contact.html


Thoughts on HipHop PHP 
=======================

:tags: c++, compile, compiler, php, programming-languages, python, unladen-swallow

This morning Facebook announced, as had been rumored for several weeks, a new, faster, implementation of PHP.  To someone, like me, who loves dynamic languages and virtual machines this type of announcement is pretty exciting, after all, if they have some new techniques for optimizing dynamic languages they can almost certainly be ported to a language I care about.  However, because of everything I've read (and learned about PHP, the language) since the announcement I'm not particularly excited about HipHop.

Firstly, there's the question of what problem HipHop solves.  It aims to improve the CPU usage of PHP applications.  For all practical purposes PHP exists exclusively to serve websites (yes, it can do other things, no one does them).  Almost every single website on the internet is I/O bound, not CPU bound, web applications spend their time waiting on external resources (databases, memcache, other HTTP resources, etc.).  So the part of me that develops websites professionally isn't super interested, Facebook is in the exceptionally rare circumstance that they've optimized their I/O to the point that `optimizing CPU gives worthwhile returns <http://en.wikipedia.org/wiki/Amdahls_law>`_.  However, the part of me that spends his evenings contributing to Unladen Swallow and hanging around PyPy still thought that there might be some interesting VM technology to explore.

The next issue for consideration was the "VM" design Facebook choose.  They've elected to compile PHP into C++, and then use a C++ compiler to get a binary out of it.  This isn't a particularly new technique, in the Python world projects like `Shedskin <http://code.google.com/p/shedskin/>`_ and `Cython <http://www.cython.org/>`_ have exploited a similar technique to get good speed ups.  However, Facebook also noted that in doing so they had dropped support for "some rarely used features â such as eval()".  An important question is which features exactly, they had dropped support for.  After all, the reason compiling a dynamic language to efficient machine code is difficult is because the dynamicism defeats the compiler's ability to optimize, but if you remove the dynamicism you remove the obstacles to efficient compilation.  However, you're also not compiling the same language.  PHP without ``eval()``, and whatever else they've removed is quite simply a different language, for this reason I don't consider either Shedskin or Cython to be an implementation of Python, because they don't implement the entire language.

This afternoon, while I was idling in the `Unladen Swallow IRC channel <irc://irc.oftc.net/unladenswallow>`_ a discussion about HipHop came up, and I learned a few things about PHP I hadn't previous realized.  The biggest of these is that a `name bound to a function in PHP cannot be undefined, or redefined <http://no.php.net/manual/en/functions.user-defined.php>`_.  If you've ever seen Collin Winter give a talk about Unladen Swallow, the canonical example of Python's dynamicism defeating a static compiler is the ``len()`` function.  For ``lists``, ``tuples``, or ``dicts`` a call to ``len()`` should be able to be optimized to a single memory read out of a field on the object, plus a call to instantiate an integer object.  However, in CPython today it's actually about 3 function calls, and 3 memory reads to get this data (plus the call to instantiate an integer object), plus the dictionary lookup in the global builtins to see what the object named ``len`` is.  That's a hell of a lot more work than a single memory read (which is one instruction on an x86 CPU).  The reason CPython needs to do all that work is that it a) doesn't know what the ``len`` object is, and b) when ``len`` is called it has no idea what its arguments will be.

As `I've written about previously <http://alexgaynor.net/2009/nov/03/diving-into-unladen-swallows-optimizations/>`_, Unladen Swallow has some creative ways to solve these problems, to avoid the dictionary lookups, and, eventually, to inline the body of the ``len()`` into the caller and optimize if for the types it's called with.  However, this requires good runtime feedback, since the compiler simply cannot know statically what any of the objects will actually be at runtime.  However, if ``len`` could be know to be the ``len()`` function at compile time Unladen Swallow could inline the body of the function, unconditionally, into the caller.  Even with only static specialization for lists, dicts, and tuples like:

.. sourcecode:: python
    
    if isinstance(obj, list):
        return obj.ob_size
    elif isinstance(obj, tuple):
        return obj.ob_size
    elif isisinstance(obj, dict):
        return obj.ma_fill
    else:
        return obj.__len__()


This would be quite a bit faster than the current amount of indirection.  In PHP's case it's actually even easier, it only has one builtin array type, which acts as both a typical array as well as a hash table.  Now extend this possibly optimization to not only every builtin, but every single function call.  Instead of the dictionary lookups Python has to do for every global these can just become direct function calls.

Because of differences like this (and the fact that PHP only has machine sized integers, not arbitrary sized ones, and not implementing features of the language such as ``eval()``) I believe that the work done on HipHop represents a fundamentally smaller challenge than that taken on by the teams working to improve the implementations of languages like Python, Ruby, or Javascript.  At the time of the writing the HipHop source has not been released, however I am interested to see how they handle garbage collection.

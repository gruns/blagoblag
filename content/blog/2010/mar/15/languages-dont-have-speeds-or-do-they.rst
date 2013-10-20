
Languages Don't Have Speeds, Or Do They? 
=========================================

:tags: compiler, programming-languages, psyco, pypy, python

Everyone knows languages don't have speeds, implementations do.  Python isn't slow; CPython is.  Javascript isn't fast; V8, Squirrelfish, and Tracemonkey are.  But what if a language was designed in such a way that it appeared that it was impossible to be implemented efficiently?  Would it be fair to say that language is slow, or would we still have to speak in terms of implementations?  For a long time I followed the conventional wisdom, that languages didn't have speeds, but lately I've come to believe that we can learn something by thinking about what the limits on how fast a language could possibly be, given a perfect implementation.

For example consider the following Python function:

.. sourcecode:: python
    
    def f(n):
        i = 0
        while i < n:
            i += 1
            n += i
        return n


And the equivilant C function:

.. sourcecode:: c
    
    int f(int n) {
        int i = 0;
        while (i < n) {
            i += 1;
            n += i;
        }
        return n;
    }


CPython probably runs this code 100 times slower than the GCC compiled version of the C code.  But we all know CPython is slow right?  PyPy or Psyco probably runs this code 2.5 times slower than the C version (I'm just spitballing here).  Psyco and PyPy are, and contain, really good just in time compilers that can profile this code, see that ``f`` is *always* called with an integer, and therefore a much more optimized version can be generated in assembly.  For example the optimized version could generate just a few ``add`` instructions in the inner loop (plus a few more instructions to check for overflow), this would skip all the indirection of calling the ``__add__`` function on integers, allocating the result on the heap, and the indirection of calling the ``__lt__`` function on integers, and maybe even some other things I missed.

But there's one thing no JIT for Python can do, no matter how brilliant.  It can't skip the check if ``n`` is an integer, because it can't prove it *always* will be an integer, someone else could import this function and call it with strings, or some custom type, or anything they felt like, so the JIT *must* verify that ``n`` is an integer before running the optimized version.  C doesn't have to do that.  It knows that ``n`` will *always* be an integer, even if you do nothing but call ``f`` until the end of the earth, GCC can be 100% positive that ``n`` is an integer.

The absolute need for at least a few guards in the resulting assembly guarantees that even the most perfect JIT compiler ever, could not generate code that was strictly faster than the GCC version.  Of course, a JIT has some advantages over a static compiler, for example, it can inline at dynamic call sites.  However, in practice I don't believe this ability is ever likely to beat a static compiler for a real world program.  On the other hand I'm not going to stop using Python any time soon, and it's going to continue to get faster, a lot faster.

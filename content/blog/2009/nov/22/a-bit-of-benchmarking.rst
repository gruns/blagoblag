
A Bit of Benchmarking
=====================

:tags: compiler, django, programming-languages, pypy, python

PyPy recently posted some `interesting benchmarks <http://morepypy.blogspot.com/2009/11/some-benchmarking.html>`_ from the computer language shootout, and in my last post about Unladen Swallow I described a patch that would hopefully be landing soon.  I decided it would be interesting to benchmarks something with this patch.  For this I used James Tauber's `Mandelbulb <http://github.com/jtauber/mandelbulb>`_ application, at both 100x100 and 200x200.  I tested CPython, Unladen Swallow Trunk, Unladen Swallow Trunk with the patch, and a recent PyPy trunk (compiled with the JIT).  My results were as follows:

============================= === ===
VM                            100 200
============================= === ===
CPython 2.6.4                 17s 64s
Unladen Swallow Trunk         16s 52s
Unladen swallow Trunk + Patch 13s 49s
PyPy Trunk                    10s 46s
============================= === ===


Interesting results.  At 100x100 PyPy smokes everything else, and the patch shows a clear benefit for Unladen.  However, at 200x200 both PyPy and the patch show diminishing returns.  I'm not clear on why this is, but my guess is that something about the increased size causes a change in the parameters that makes the generated code less efficient for some reason.

It's important to note that Unladen Swallow has been far less focussed on numeric benchmarks than PyPy, instead focusing on more web app concerns (like template languages).  I plan to benchmark some of these as time goes on, particularly after PyPy merges their "faster-raise" branch, which I'm told improves PyPy's performance on Django's template language dramatically.

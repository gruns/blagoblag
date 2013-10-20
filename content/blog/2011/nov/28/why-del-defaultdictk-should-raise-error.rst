
Why del defaultdict()[k] should raise an error 
===============================================


Raymond Hettinger recently asked on twitter what people thought
``del defaultdict()[k]`` did for a ``k`` that didn't exist in the ``dict``. 
There are two ways of thinking about this, one is, "it's a defaultdict, there's
always a value at a key, so it can never raise a KeyError", the other is, "that
only applies to reading a value, this should still raise an error".  I
initially spent several minutes considering which made more sense, but I
eventually came around to the second view, I'm going to explain why.

The Zen of Python says, "Errors should never pass silently."  Any Java
programmer who's seen ``NullPointerException`` knows the result of passing
around invalid data, rather than propagating an error.  There are two cases for
trying to delete a key which doesn't exist in a ``defaultdict``.  One is: "this
algorithm happens to sometimes produce keys that aren't there, not an issue,
ignore it", the other is "my algorithm has a bug, it should always produce
valid keys".  If you don't raise a ``KeyError`` the first case has a single
line of nice code, if you do raise an error they have a boring ``try``/
``except KeyError`` thing going on, but no big loss.  However, if an error
isn't raised **and** your algorithm should never produce nonexistent keys,
you'll be silently missing a large bug in your algorithm, which you'll have to
hope to catch later.

The inconvenience of ignoring the ``KeyError`` to the programmer with the
algorithm that produces nonexistent keys is out weighed by the potential for
hiding a nasty bug in the algorithm of the programmer who's code should never 
produce these.  Ignoring an exception is easy, trying to find the bug in your 
algorithm can be a pain in the ass.

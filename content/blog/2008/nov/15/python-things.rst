
Python Things
=============


I wasn't really sure what to name today's post, but it's basically going to be nifty things you can do in Python, and general tips.

 * SystemExit, sys.exit() raises SystemExit, if you actually want to keep going, you can just catch this exception, nothing special about it.
 * iter(callable, terminal), basically if you use iter in this way, it will keep calling the callable until the callable returns terminal, than it beaks.
 * a &lt; x &lt; b , in Python you can chain comparison operators like this.  That's the same as writing a &lt; x and x &lt; b.

 * dict(), amongst the other ways to instantiate a dictionary in Python, you can give it a list of two tuples, so for example, [('a', 2), ('b', 3')] becomes {'a': 2, 'b': 3}.
 * open(filename), is an iterable, each iteration yields another line.
 * If you don't need ordering, use set() instead of list().  set() has better runtime for just about every operation, so if you don't need the ordering, use it.
 * Python comes with turtle graphics.  This probably doesn't matter to most people, but if you want to help get a kid into programming, import turtle can be a great way.
 * pdb, the Python debugger is simply invaluable, try: code that isn't working, except ExceptionThatGetsRaised: import pdb; pdb.set_trace() is all it takes to get started with the itneractive debugger.
 * webbrowser.open(url), this module is just cool, it opens up the users browser to the desired URL.

And those are my tips!  Please share yours.

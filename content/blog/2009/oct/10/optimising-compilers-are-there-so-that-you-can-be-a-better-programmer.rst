
Optimising compilers are there so that you can be a better programmer
=====================================================================


In a discussion on the Django developers mailing list I recently commented that the performance impact of having logging infrastructure, in the case where the user doesn't want the logging, could essentially be disregarded because Unladen Swallow (and PyPy) are bringing us a proper optimising (Just in Time) compiler that would essentially remove that consideration.  Shortly thereafter someone asked me if I really thought it was the job of the interpreter/compiler to make us not think about performance.  And my answer is: the job of a compiler is to let me program with best practices and not suffer performance consequences for doing things the right way.

Let us consider the most common compiler optimisations.  A relatively simple one is function inlining, in the case where including the body of the function would be more efficient than actually calling it, a compiler can simply move the functions body into its caller.  However, we can actually do this optimisation in our own code.  We could rewrite:


.. sourcecode:: python
    
        def times_2(x):
            return x * 2
    
        def do_some_stuff(i):
            for x in i:
                # stuff
                z = times_2(x)
            # more stuff

as:


.. sourcecode:: python
    
        def do_some_stuff(i):
            for x in i:
                # stuff
                z = x * 2
            # more stuff

And this is a trivial change to make.  However in the case where ``times_2`` is slightly less trivial, and is used a lot in our codebase it would be exceptionally more programming practice to repeat this logic all over the place, what if we needed to change it down the road?  Then we'd have to review our entire codebase to make sure we changed it everywhere.  Needless to say that would suck.  However, we don't want to give up the performance gain from inlining this function either.  So here it's the job of the compiler to make sure functions are inlined when possible, that way we get the best possible performance, as well as allowing us to maintain our clean codebase.

Another common compiler optimisation is to transform multiplications by powers of 2 into binary shifts.  Thus ``x * 2`` becomes ``x << 1``
A final optimisation we will consider is constant propagation.  Many program have constants that are used throughout the codebase.  These are often simple global variables.  However, once again, inlining them into methods that use them could provide a significant benefit, by not requiring the code to making a lookup in the global scope whenever they are used.  But we really don't want to do that by hand, as it makes our code less readable ("Why are we multiplying this value by  this random float?", "You mean pi?", "Oh."), and makes it more difficult to update down the road.  Once again our compiler is capable of saving the day, when it can detect a value is a constant it can propagate it throughout the code.

So does all of this mean we should never have to think about writing optimal code, the compiler can solve all problems for us?  The answer to this is a resounding no.  A compiler isn't going to rewrite your insertion sort into Tim sort, nor is it going to fix the fact that you do 700 SQL queries to render your homepage.  What the compiler can do is allow you to maintain good programming practices.

So what does this mean for logging in Django?  Fundamentally it means that we shouldn't be concerned with possible overhead from calls that do nothing (in the case where we don't care about the logging) since a good compiler will be able to eliminate those for us.  In the case where we actually do want to do something (say write the log to a file) the overhead is unavoidable, we have to open a file and write to it, there's no way to optimise it out.

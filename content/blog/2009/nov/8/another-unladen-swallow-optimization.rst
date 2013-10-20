
Another Unladen Swallow Optimization
====================================


This past week I described a few optimizations that the Unladen Swallow team have done in order to speed up CPython.  In particular one of the optimizations I described was to emit direct calls to C functions that took either zero or one argument.  This improves the speed of Python when calling functions like len() or repr(), who only take one argument.  However, there are plenty of builtin functions that take a fixed number of arguments that is greater than one.  This is the source of the latest optimization.

As I discussed previously there were two relevant flags, METH_O and METH_NOARGS.  These described functions that take either one or zero arguments.  However, this doesn't cover a wide gamut of functions.  Therefore the first stage of these optimizations was to replace these two flags with METH_FIXED, which indicates that the function takes a fixed number of arguments.  There was also an additional slot added to the struct that holds C functions to store the arity of the function (the number of arguments it takes).  Therefore something like:

.. sourcecode:: python
    
        {"id", builtin_id, METH_O, id_doc}

Which is what the struct for a C function looks like would be replaced with:

.. sourcecode:: python
    
        {"id", builtin_id, METH_FIXED, id_doc, 1}

This allows Unladen Swallow to emit direct calls to functions that take more than 1 argument, specifically up to 3 arguments.  This results in functions like hasattr() and setattr() to be better optimized.  This change ultimately results in a 7% speed increase in Unladen Swallow's Django benchmark.  Here the speed gains will largely come from avoiding allocating a tuple for the arguments, as Python used to have to do since the functions were defined as METH_VARARGS (which results in it receiving it's arguments as a tuple), as well as avoiding parsing that tuple.

This change isn't as powerful as it could be, specifically it requires that the function always take the same number of arguments.  This prevents optimizing calls to getattr() for example, which can take either 2 or 3 arguments.  This optimization doesn't hold because C doesn't have any way of expressing default arguments for the function, therefore the CPython runtime must pass all of the needed arguments to a function, which means C functions need to have a way to encode their defaults in a way that CPython can understand.  One of the proposed solutions to this problem is to have functions be able to provide the minimum number of arguments they take and then CPython could pad the provided arguments with NULLs to achieve the correct number of arguments to the function (interestingly the C standard allows more arguments to be passed to a function than it takes).  This type of optimization would speed up calls to things like dict.get() and getattr().

As you can see the speed of a Python application can be fairly sensitive to how various internal things are handled, in this case the speed increase can be shown to come exclusively from eliminating a tuple allocation and some extra logic on certain function calls.  If you're interested in seeing the `full changeset it's available on the internet. <http://code.google.com/p/unladen-swallow/source/detail?r=890>`_

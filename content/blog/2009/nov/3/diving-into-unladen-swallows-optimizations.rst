
Diving into Unladen Swallow's Optimizations
===========================================


Yesterday I described the general architecture of Unladen Swallow, and I said that just by switching to a JIT compiler and removing the interpretation overhead Unladen Swallow was able to get a performance gain.  However, that gain is nowhere near what the engineers at Google are hoping to accomplish, and as such they've been working on building various optimizations into their JIT.  Here I'm going to describe two particularly interesting ones they implemented during the 3rd quarter (they're doing quarterly releases).

Before diving into the optimizations themselves I should note there's one piece of the Unladen Swallow architecture I didn't discuss in yesterday's post.  The nature of dynamic languages is that given code can do nearly anything depending on the types of the variables present, however in practice usually very few types are seen.  Therefore it is necessary to collect information about the types seen in practice in order to perform optimizations.  Therefore what Unladen Swallow has done is added data collection to the interpreter while it is executing bytecode.  For example the BINARY_ADD opcode records the types of both of it's operands, the CALL_FUNCTION opcode records the function it is calling, and the UNPACK_SEQUENCE opcode records the type of the sequence it's unpacking.  This data is then used when the function is compiled to generate optimal code for the most likely scenarios.

The first optimization I'm going to look at is one for the CALL_FUNCTION opcode.  Python has a number of flags that functions defined in C can have, the two relevant to this optimization are METH_NOARGS and METHO_O.  These flags indicate that the function (or method) in question take either 0 or 1 argument respectively (this is excluding the self argument on methods).  Normally when Python calls a function it builds up a tuple of the arguments, and a dictionary for keyword arguments.  For functions defined in Python CPython lines up the arguments with those the function takes and then sets them as local variables for the new function.  For C functions they are given the tuple and dictionary directly and are responsible for parsing them themselves.  By contrast functions with METH_NOARGS or METH_O receive their arguments (or nothing in the case of METH_NOARGS) directly.

Because calling METH_NOARGS and METH_O functions is so much easier than the alternate case (which involves several allocations and complex logic) when possible it is best to special case them in the generated assembly.  Therefore, when compiling a CALL_FUNCTION opcode if using the data recorded there is only ever one function called (imagine a call to len, it is going to be the same len function every time), and that function is METH_NOARGS or METH_O then instead of generating a call to the usual function call machinery Unladen Swallow instead emits a check to make sure the function is actually the expected one and if it passes emits a call directly to the function with the correct arguments.  If this guard fails then Unladen Swallow jumps back to the regular interpreter, leaving the optimized assembly.  The reason for this is that the ultimately generated assembly can be more efficient when it only has to consider one best case scenario, as opposed to needing to deal with a large series of if else statements, which catalogue every single best case and the corresponding normal case.  Ultimately, this results in more efficient code for calls to functions like len(), which are basically never redefined.

The next optimization we're going to look at is one for the LOAD_GLOBAL function.  The LOAD_GLOBAL  opcode is used for getting the value of a global variable, such as a builtin function, an imported class, or a global variable in the same module.  In the interpreter the code for this opcode looks something like:

.. sourcecode:: python
    
        name = OPARG()
        try:
            value = globals[name]
        except KeyError:
            try:
                value = builtins[name]
            except KeyError:
                raise_exception(KeyError, name)
        PUSH(value)

As you can see in the case of a builtin object (something like len, str, or dict) there are two dictionary lookups.  While the Python dictionary is an exceptionally optimized datastructure it still isn't fast compared to a lookup of a local value (which is a single lookup in a C array).  Therefore the goal of this optimization is to reduce the number of dictionary lookups needed to find the value for a global or builtin.

The way this was done was for code objects (the datastructures that hold the opcodes and various other internal details for functions) to register themselves with the globals and builtin dictionaries.  By registering themselves the dictionaries are able to notify the code objects (similar to Django signals) whenever they are modified.  The result of this is that the generated assembly for a LOAD_GLOBAL can perform the dictionary lookup once at compilation time and then the resulting assembly will be valid until the globals or builtins dictionary notifies the code object that they have been modified, thus rendering the assembly invalid.  In practice this is very efficient because globals and builtins are very rarely modified.

Hopefully you've gotten a sense of the type of work that the people behind Unladen Swallow are doing.  If you're interested in reading more on this type of work I'd highly recommend taking a look at the literature listed on the `Unladen Swallow wiki <http://code.google.com/p/unladen-swallow/wiki/RelevantPapers>`_, as they note that there is no attempt to do any original research, all the work being done is simply the application of existing, proven techniques to the CPython interpreter.

For the rest of this month I'm going to try to give a preview of the next day's post with each post, that way I can start thinking about it well in advance.  Tomorrow I'm going to shift gears a little bit and write about the ManyToManyField refactoring I did over the summer and which was just committed to Django.

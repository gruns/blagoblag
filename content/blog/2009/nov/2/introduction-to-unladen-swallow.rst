
Introduction to Unladen Swallow
===============================


Unless you've been living under a rock for the past year (or have zero interest in either Python or dynamic languages, it which case why are you here?) you've probably heard of Unladen Swallow.  Unladen Swallow is a Google funded branch of the CPython interpreter, with a goal of making CPython significantly faster while retaining both API and ABI compatibility.  In this post I'm going to try to explain what it is Unladen Swallow is doing to bring a new burst of speed to the Python world.

In terms of virtual machines there are a few levels of complexity, which roughly correspond to their speed.  The simplest type of interpreter is an AST evaluator, these are more or less the lowest of the low on the speed totem pole, up until YARV was merged into the main Ruby interpreter, MRI (Matz Ruby Interpreter) was this type of virtual machine.  The next level of VM is a bytecode interpreter, this means that the language is compiled to an intermediary format (bytecode) which is then executed.  Strictly speaking this is an exceptionally broad category which encompasses most virtual machines today, however for the purposes of this article I'm going to exclude any VMs with a Just-In-Time compiler from this section (more on them later).  The current CPython VM is this type of interpreter.  The most complex (and fastest) type of virtual machine is one with a Just-In-Time compiler, this means that the bytecode that the virtual machine interprets is also dynamically compiled into assembly and executed.  This type of VM includes modern Javascript interpreters such as V8, Tracemonkey, and Squirellfish, as well as other VMs like the Hotspot Java virtual machine.

Now that we know where CPython is, and what the top of the totem pole looks like it's probably clear what Unladen Swallow is looking to accomplish, however there is a bit of prior art here that's worthy of taking a look.  There is actually currently a JIT for CPython, named Psyco.  Psyco is pretty commonly used to speed up numerical code, as that's what it's best at, but it can speed up most of the Python language.  However, Psyco is extremely difficult to maintain and update.  It only recently gained support for modern Python language features like generators, and it still only supports x86 CPUs.  For these reasons the developers at Google chose to build their JIT rather than work to improve the existing solution (they also chose not to use one of the alternative Python VMs, I'll be discussing these in another post).

I just said that Unladen Swallow looked to build their own JIT, but that's not entirely true.  The developers have chosen not to develop their own JIT (meaning their own assembly generator, and register allocator, and optimizer, and everything else that goes along with a JIT), they have instead chosen to utilize the LLVM (Low Level Virtual Machine) JIT for all the code generation.  What this means is that instead of doing all the work I've alluded the devs can instead translate the CPython bytecode into LLVM IR (intermediate representation) and then use LLVM's existing JIT infrastructure to do some of the heavy lifting.  This gives the devs more time to focus on the interesting work of how to optimize the Python language.

Now that I've layed out the background I'm going to dive into what exactly it is that Unladen Swallow does.  Right now the CPython virtual machine looks something like this:

.. sourcecode:: python
    
        for opcode in opcodes:
            if opcode == BINARY_ADD:
                x, y = POP(), POP()
                z = x + y
                PUSH(z)
            elif opcode == JUMP_ABSOLUTE:
                pc = OPARG()
            # ...

This is both hugely simplified and translated into a Pythonesque psuedocode, but hopefully it makes the point clear, right now the CPython VM runs through the opcodes and based on what the opcode is executes some C code.  This is particularly inefficient because there is a fairly substantial overhead to actually doing the dispatch on the opcode.  What Unladen Swallow does is count the number of times a given Python function is called (the heuristic is actually slightly more complicated than this, but it's a good approximation of what happens), and when it reaches 10000 (the same value the JVM uses) it stops to compile the function using LLVM.  Here what it does is essentially unrolls the interpreter loop, into the LLVM IR.  So if you had the bytecode:

.. sourcecode:: python
    
        BINARY_ADD

Unladen Swallow would generate code like:

.. sourcecode:: python
    
        x, y = POP(), POP()
        z = x + y
        PUSH(z)

This eliminates all of the overhead of the large loop in the interpreter.  Unladen Swallow also performs a number of optimizations based on Python's semantics, but I'll be getting into those in another post, for now LLVM run it's optimizers, which can improve the generated code somewhat, and then CPython executes the generated function.  Now whenever this function is called in the future the optimized, assembly version of it is called.

This concludes the introduction to Unladen Swallow.  Hopefully you've learned something about the CPython VM, Unladen Swallow, or virtual machines in general.  In future posts I'm going to be diving in to some of the optimizations Unladen Swallow does, as well as what other players are doing in this space (particularly PyPy).

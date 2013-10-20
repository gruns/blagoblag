
Why I'm not very excited about Go
=================================

:tags: c++, compiler, go, programming-languages

When I first heard Rob Pike and Ken Thompson had created a new programming language my first instinct is, "I'm sure it'll be cool, these are brilliant guys!"  Unfortunately that is not the case, mostly because I think they made some bad design choices, and because the "cool new things" aren't actually that new, or cool.

The first major mistake was using a C derived syntax: braces and semicolons.  I know some people don't like significant whitespace, but if you aren't properly indenting your code it's already beyond the point of hopelessness.  The parser ought to use the existing structure instead of adding more punctuation.  Readability is one of the most important attributes of code, and this syntax detracts from that.

The next mistake is having a separate declaration and assignment operator.  I understand that the point of this operator is to reduce the repetition of typing out the types name both in declaring the variable and in initializing the value.  Yet it seems the purpose of the := operator is to avoid typos in variable names that are possible by making all assignment an implicit declaration if the variable wasn't already declared.  I can see myself making many more typos by forgetting to use the := operator, and in cases where I make a typo in a variable name it would inevitably be caught by the compiler when I attempted to actually use it (the fact that this is an attempted declaration means the variable won't have been declared elsewhere).

The final mistake was not providing generics.  C++'s templates is one of the things that make the language head and shoulders more useful for me than C for tasks I need to preform; generics allow one to provide reusable data structures.  While Go seems to have something akin to generics with their map data structure, it disappointingly doesn't appear to be exposed in any way to user code.  One of the things I've found makes me most productive in Python is that any time I need to perform a task I simply pick the data structure that does what I want and it is efficiently implemented.  Without generics, I don't see a way for a statically typed language to offer this same breadth of data structures without each of them being a special case.

In terms of features which I believe are overhyped the most important one is the "goroutine".  As best I can tell these are an implementation of `fibers <http://en.wikipedia.org/wiki/Fiber_(computer_science)>`_.  Constructs like concurrency should not be granted their own syntax, especially when they can be cleanly implemented using the other constructs of a language, look at the C library `libtask <http://swtch.com/libtask/>`_ as an example.

Further, the handling of interfaces, though interesting, appears to be an implementation of C++0x's proposed concepts (which won't be in the final standard).  I view this feature as something that is most useful in the context of generics, which Go doesn't have.  The reason for this is to be able to make compile time assertions about the types that are being templated over.  Doing anything else is more clearly implemented as abstract inheritance.

I'm not writing off Go permanently, but I'm not enthused about it, someone will probably have to let me know when I need to look again as I won't be following along.  Enjoy your internet travels.


Building a Programming Language with Python
===========================================

:tags: compile, ply, python

One of my side projects of late has been building a programming language in Python, using the PLY library.  PLY is essentially a Python implementation of the classic Lex and Yacc tools.  The language, at present, has a syntax almost exactly the same as Python's (the notable difference, in so far as features that have been implemented, is that you are not allowed to have multiple statements on the same line, or to put anything following a colon on the same line).  The language(currently called 'Al' although that's more of a working name), is a dynamic language that builds up an syntax tree for the code, and than executes it.  However, the long term goal is to have it actually be a compiled language, similar to Lisp or C.  Essentially the mechanism for doing this will be the same as how a C++ compiler handles multiple dispatch, which is dynamically at run time.

At present however, this mythical fully compiled language is far from complete, I haven't even began to think about the assembly generation, mostly because I don't know assembly at all, and one of the courses I will be taking next semester is one which covers assembly code.  However, the question that has to be asked, are what are the advantages of a compiled language, and what are the costs?

First the benefits:

 * It's faster, even a worst case C++ program that fully utilizes multiple dispatch at runtime will go faster than a program using the same algorithms in Python.
 * You get an executable at the end. This is a huge advantage for distribution, you don't need to distribute the source code, and you have an exe to give to people.

There are probably others, but I'm assuming the semantics of a language similar to Python, so I haven't included things like compile time type checking. And now the disadvantages:

 * You lose some of the dynamicism. Doing things like eval(), or dynamic imports is inherently harder, if not impossible.
 * You lose the REPL (interactive interpreter).

So can we overcome those? As far as I can tell the first should be doable, eval() necessitates the inclusion of an interpreter with the language, the thought of this already has to be making people think this is just going to end up as a VM. But, I think this can be overcome, we can know, at compile time, whether or not a user will be using eval, and decide then whether or not to compile the interpreter and link against it. Dynamic imports are, if anything harder, I think, I think this is just an issue of doing run time linking, but I'm not sure. As for the issue of the REPL, this is a non-issue as far as I'm concerned, there is no inherent reason a compiled language can't have a REPL, we just often don't, languages like Common Lisp have long had both.

So now, let's see some code. I hope to have some code to show off, that handles at least a subset of Python, for PyCon 2009, as work begins on assembly generation I will post here. For anyone interested in the code at present, you can see it `here <http://github.com/alex/alex-s-language/tree/master>`_.

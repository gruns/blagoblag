
The run-time distinction 
=========================

:tags: programming, programming-languages, python

At `PyCodeConf`_ I had a very interesting discussion with `Nick Coghlan`_ which
helped me understand something that had long frustrated me with programming
languages.  Anyone who's ever taught a new programmer Java knows this, but
perhaps hasn't understood it for what it is.  This thing that I hadn't been
appreciating was the distinction some programming languages make between the
language that exists at compile time, and the language that exists at run-time.

Take a look at this piece of Java code:

.. sourcecode:: java

    class MyFirstProgram {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }

Most people don't appreciate it, but you're really writing in two programming
languages here, one of these languages has things like class and function
declarations, and the other has executable statements (and yes, I realize Java
has anonymous classes, they don't meaningfully provide anything I'm about to
discuss).

Compare that with the (approximately) equivalent Python code:

.. sourcecode:: python

    def main():
        print "Hello World"

    if __name__ == "__main__":
        main()

There's a very important thing to note here, we have executable statements at
the top level, something that's simply impossible in Java, C, or C++. They make
a distinction between the top level and your function's bodies. It follows from
this that the function we've defined doesn't have special status by virtue of
being at the top level, we could define a function or write a class in any
scope. And this is important, because it gives us the ability to express things
like decorators (both class and function).

Another example of this distinction that `James Tauber`_ pointed out to me is
the ``import`` statement. In Python is it a line of executable code which
invokes machinery in the VM to find a module and load it into the current
namespace. In Java it is an indication to the compiler that a certain symbol is
in scope, it's never executed.

Why would anyone care about this distinction though? It's clearly possibly to
write programs in languages on both ends of the spectrum. It appears to me that
the expressiveness of a programming language is really a description of what
the distance between the compile time language and the runtime language is.
Python stands on one end, with no distinction, whereas C/C++/Java stand on the
other, with a grand canyon separating them.

But what about a language in the middle? Much of PyPy's code is written in a
language named RPython. It has a fairly interesting property though, its
run-time language is pretty close to Java in semantics, it's statically typed
(though type inferenced), it's compile time language is Python. In practice
this means you get many of the benefits in expressiveness as you do from using
Python itself. For example you can write a decorator, or generate a class. A
good example of this power is in `PyPy's NumPy implementation`_. We're able to
create the code for doing all the operations on different dtypes (NumPy's name
for the different datatypes its arrays can represent) dynamically, without
needing to resort to code generation or repeating ourselves, we're able to rely
on Python as our compile time (or meta-programming) language. The "in-practice" result of this is that writing RPython feels much more like writing Python than it does like writing Java, even though most of your code is written under the same constraints (albeit without the need to explicitly write types).

The distinction between compile-time and run-time in programming languages
results in both more pain for programmers, as well as more arcane structures to
explain to new users. I believe new languages going forward should make it a
goal to either minimize this difference (as Python does) or outfit languages
with more powerful compile-time languages which give them the ability to
express meta-programming constructs.

.. _`PyCodeConf`: http://py.codeconf.com/
.. _`Nick Coghlan`: https://twitter.com/#!/ncoghlan_dev
.. _`James Tauber`: https://twitter.com/#!/jtauber
.. _`PyPy's NumPy implementation`: https://bitbucket.org/pypy/pypy/src/default/pypy/module/micronumpy/interp_dtype.py

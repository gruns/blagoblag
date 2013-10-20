
A statically typed language I'd actually want to use
====================================================


Nearly a year ago I tweeted, and released on `github <https://github.com/alex/shore>`_ a project I'd been working.  It's called shore, and it's the start of a compiler for a statically typed language I'd actually like to use.  Programming is, for me, most fun when I can work at the level that suits the problem I have: when I'm building a website I don't like to think about how my file system library is implemented.  That means a language needs to support certain abstractions, and it also needs to be sufficiently concise that I'd actually want to write things in.  A good example is "give me the square of all the items in this sequence who are divisible by 3", in Python:

.. sourcecode:: python

    [x * x for x in seq if x % 3 == 0]

And in C++:

.. sourcecode:: c++

    std::vector<int> result;
    for (std::vector<int>::iterator itr = seq.begin(); itr != seq.end(); ++itr) {
        if (*itr % 3 == 0) {
            result.push_back((*itr) * (*itr));
        }
    }

The best I can say for that is: what the hell.  There's nothing that's not static about my Python code (assuming the compiler knows that ``seq`` is a list of integers), and yet... it's a fifth as many lines of code, and significantly simpler (and requires no changes if I put my integers in a different sequence).

The point of shore was to bring these higher level syntactic constructs, static typing, and support for higher level abstractions into a single programming language.  The result was to be an explicitly statically typed, ahead of time compiled, garbage collected language.

The syntax is inspired almost exclusively by Python and the type system is largely inspired by C++ (except there are no primitive, everything is an object).  For example here's a function which does what those two code snippets do:

.. sourcecode:: c++
    
    list{int} def play_with_seq(list{int} seq):
        return [x * x for x in seq if x % 3 == 0]

As you can see it support parametric polymorphism (templating).  One important piece of this is the ability to operate on more abstract types.  For example this could be rewritten:

.. sourcecode:: c++

    list{int} def playwith_seq(iterable{int} seq):
        return [x * x for x in seq if x % 3 == 0]

``iterable`` is anything that implements the iterator protocol.

I'll be writing more about my thoughts on the language as the month goes on, however I need to stress the implementation is both a) untouched since December, and b) nothing you want to look at, it's a working lexer, mostly working parser, and a terrible translator into C++.  However, I hope this can inspire people to work towards a more perfect statically typed language.


Getting Started With PLY
========================

:tags: lex, ply, python

The other day I mentioned I was using PLY in my post about building a language, so today I'm going to describe getting started with PLY, specifically the tokenization phase. For those who don't know much about parsing a language, the tokenization phase is where we take the source file, and turn it into a series of tokens. For example, turning a = 3 + 4 into, NAME EQUALS 3 PLUS 4. As you can see that simple assignment becomes 5 tokens, each number is a token, both numbers are tokens, and a is a NAME token. So how do we do this in PLY?

PLY's method for defining tokenization rules is very creative. First you define a list of tokens, for example:

.. sourcecode:: python

    tokens = (
       'NUMBER',
       'PLUS',
       'MINUS',
       'TIMES',
       'DIVIDE',
    )

Here we have defined the types of tokens we will define, what each of these is should be self explanatory. Then we define some rules, they look like this:

.. sourcecode:: python

    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_DIVIDE  = r'/'
    def t_NUMBER(t):
        r'\d+'
        try:
            t.value = int(t.value)    
        except ValueError:
            t.value = 0
        return t

This is probably less obvious. There are 2 ways to define the rules for a token, either as a string, or as a function. Either way they are named t_TOKEN_NAME. For a lot of tokens you can just do the string, those are the ones that don't require processing, and the string is just a regex that matches the token. For things that do need processing, we can define a function. The function takes 1 parameter, which is a lexer object, as you can see in our example, we take in t, and since we are defining a number token we set the value to be the integer for the string representation from the source code. The interesting thing here is how we define the rule for, PLY uses the docstring for a function to get the regex for it.

Now that we have all of our rules set up we need to actually build the lexer object:

.. sourcecode:: python

    lexer = lex.lex()

And then we can use the input() function on a lexer to provide the source code, and the token function to pop the next token off the lexer.

That's all for today, in the future we'll take a look at the other components of building the grammar of a language, and at how we implement it. For more information now, PLY has excellent documentation, available here.

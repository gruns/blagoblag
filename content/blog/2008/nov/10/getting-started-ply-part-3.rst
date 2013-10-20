
Getting Started With PLY - Part 3
=================================


As promised, today we'll be looking at implementing additional arithmetic operations, dealing with order of operations, and adding variables to our languages, so without further ado, let's jump into the code.

We can replace our old addition rule with this:

.. sourcecode:: python

    import operator
    def p_expression_arithmetic(p):
       '''
       expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
       '''
       OPS = {
           '+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.div
       }
       p[0] = OPS[p[2]](p[1], p[3])

Hopefully what this code does is pretty clear, the | operator in the rule is an or option.  So if we match any of these, we get the correct function out of our ops dictionary(if you aren't familiar with operator module check it out, it's awesome), and then call it with the two arguments.

This handles the arithmetic correctly, but doesn't handle order of operations, so lets add that in:

.. sourcecode:: python

    precedence = (
       ('left', 'PLUS', 'MINUS'),
       ('left', 'TIMES', 'DIVIDE'),
    )

What this says is all these operations are left-associative, and TIMES and DIVIDE have a high precedence than PLUS and MINUS(both groupings have equal precedence, and thus read left to right).

Now that we have a fully functioning calculator, let's add in variables, first we need to add a token for NAMES (variables) and for the assignment operator:

.. sourcecode:: python

    def t_NAME(t):
       r'[a-zA-Z_][a-zA-Z_0-9]*'
       return t

    t_EQ = r'='

And of course add NAME and EQ to the list of tokens, and now a few parsing rules:

.. sourcecode:: python

    names = {}

    def p_expression_name(p):
       '''
       expression : NAME
       '''
       p[0] = names[p[1]]

    def p_assignment(p):
       '''
       assignment : NAME EQ expression
       '''
       names[p[1]] = p[3]

So here we define a names dictionary, it will map variables to values.  Hopefully the parse rules are fairly obvious, and everything makes sense.

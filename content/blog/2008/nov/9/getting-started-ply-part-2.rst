
Getting Started With PLY - Part 2
=================================

:tags: ply, python, yacc

Yesterday we created our tokens, and using these we can parse our language (which right now is a calculator) into some tokens. Unfortunately this isn't very useful. So today we are going to start writing a grammar, and building an interpreter around it.

In PLY, grammar rules are defined similarly to tokens, that is, using docstrings. Here's what a few grammar rules for out language might look like:

.. sourcecode:: python

    def p_expression_plus(p):
        '''
        expression : expression PLUS expression
        '''
        p[0] = p[1] + t[3]

    def p_expression_number(p):
        '''
        expression : NUMBER
        '''
        p[0] = [1]

So the first docstring works is, an expression is defined as expression PLUS expression.  Here PLUS is the token we defined earlier, and expression is any other way we've defined expression, so an expression is also a number (which is the token we defined earlier).  The way the code works is essentially that p[0] is the result, and each piece of the definition is it's own subscript, so p[1] and p[3] refer to the two expression in the plus expression we defined.

To actually use this parser we've defined we do:

.. sourcecode:: python

    parser = yacc.yacc()
    if __name__ == '__main__':
       while True:
           try:
               s = raw_input('calc > ')
           except EOFError:
               break
           if not s:
               continue
           result = parser.parse(s)
           print result

Try it out!  As an exercise, the reader can implement other operations (remember the order of operations!), and perhaps variables.  Tomorrow, I'll be discussing implementing these.  As always, the PLY documentation is excellent, and available `here <http://www.dabeaz.com/ply/ply.html>`_.

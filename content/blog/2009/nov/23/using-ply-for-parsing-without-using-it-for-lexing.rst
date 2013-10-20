
Using PLY for Parsing Without Using it for Lexing
=================================================


Over the past week or so I've been struggling with attempting to write my own parser (or parser generator) by hand.  A few days ago I finally decided to give up on this notion (after all the parser isn't my end goal) as it was draining my time from the interesting work to be done.  However, I wanted to keep my existing lexer.  I wrote the lexer by hand in the method I described in a previous post, it's fast, easy to read, and I rather like my handiwork, so I wanted to keep it if possible.  I've used PLY before (as I described last year) so I set out to see if it would be possible to use it for parsing without using it for lexing.

As it turns out PLY expects only a very minimal interface from it's lexer.  In fact it only needs one method, token(), which returns a new token (or None at the end).  Tokens are expected to have just 4 attributes.  Having this knowledge I now set out to write a pair of compatibility classes for my existing lexer and token classes, I wanted to do this without altering the lexer/token API so that if and when I finally write my own parser I don't have to remove legacy compatibility stuff.  My compatibility classes are very small, just this:

.. sourcecode:: python
    
        class PLYCompatLexer(object):
            def __init__(self, text):
                self.text = text
                self.token_stream = Lexer(text).parse()
    
            def token(self):
                try:
                    return PLYCompatToken(self.token_stream.next())
                except StopIteration:
                    return None
    
    
        class PLYCompatToken(object):
            def __init__(self, token):
                self.type = token.name
                self.value = token.value
                self.lineno = None
                self.lexpos = None
    
            def __repr__(self):
                return "<Token: %r %r>" % (self.type, self.value)

This is the entirety of the API that PLY needs.  Now I can write my parser exactly as I would normally with PLY.

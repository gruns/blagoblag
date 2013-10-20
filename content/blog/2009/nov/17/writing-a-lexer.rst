
Writing a Lexer
===============

:tags: compile, lex, parse, programming-languages, python

People who have been reading this blog since last year (good lord) may recall that once upon a time I did a short series of posts on lexing and parsing using PLY.  Back then I was working on a language named Al.  This past week or so I've started working on another personal project (not public yet) and I've once again had the need to lex things, but this time I wrote my lexer by hand, instead of using any sort of generator.  This has been an exceptional learning experience, so I'd like to pass some of that on to you.

The first thing to note is that writing a lexer is a great place to TDD (test driven development), I've rewritten various parts of my lexer five or more times, I've needed my tests to keep me sane.  Got your tests written?  Ok it's time to dive right into our lexer.

I've structured my lexer as a single class that takes an input string, and has a parse method which returns a generator that yields tokens (tokens are just a namedtuple with a name and value field).  The parser has two important attributes, state which is a string that says what state the lexer is in (this is used for tokens that are more than one character long), and current_val which is a list containing characters that will eventually become the value for the current token being found.

The parse method iterates through characters in the text and then it checks, if the parser has a state (self.state is not None) it does getattr(self, self.state)(character).  Otherwise it calls self.generic(character).  Then the various "state methods" are responsible for mutating self.current_val and self.state and returning a Token.  So for example the string state looks like this:

.. sourcecode:: python
    
        def string(self, ch):
            if ch == '"':
                sym = Symbol("STRING", "".join(self.current_val))
                self.current_val = []
                self.state = None
                return sym
            elif ch == "\\":
                self.state = "string_escaped"
            else:
                self.current_val.append(ch)

If the character is a quote then we're closing our string so we return our string Symbol, reset the current_val and state.  If the character is a \ then we switch into a string_escaped state which knows to handle the character as a literal and then go back to string state.  If the character is anything else then we just append it to the current_val, it will get handled at the end of the string.

I've found this to be an exceptionally powerful method, and it makes my end result code very readable.  Hopefully I'll be able to reveal my project in the coming weeks, as I'm very excited about it, even if it's not ready I'll continue to share these lessons learned as I go.

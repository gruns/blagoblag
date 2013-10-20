
What Python learned from economics
==================================


I find economics to be a fairly interesting subject, mind you I'm bored out of my mind about hearing about the stock markets, derivatives, and whatever else is on CNBC, but I find what guys like Steven Levitt and Steve E. Landsburg do to be fascinating.  A lot of what they write about is why people do what they do, and how to incentivise people to do the right thing.  Yesterday I was reading through David Goodger's `Code Like a Pythonista <http://python.net/%7Egoodger/projects/pycon/2007/idiomatic/>`_ when I got to this portion:

    LUKE: Is from module import * better than explicit imports?

    YODA: No, not better.  Quicker, easier, more seductive.

    LUKE: But how will I know why explicit imports are better than the wild-card form?

    YODA: Know you will when your code you try to read six months from now.

And I realized that Python had learned a lot from these economists.

It's often dificult for a programmer to see the advantage of doing something the right way, which will be benneficial in six months, over just getting something done now.  However, Python enforces doing things the right way, and when doing things the right way is just as easy as doing in the wrong way, you make the intuitive decision of doing things the right way.  Almost every code base I've worked with(outside of Python) had some basic indentation rules that the code observed, Python just encodes this into the language, which requires all code to have a certain level of readability.

Django has also learned this lesson.  For example, the template language flat out prevents you from putting your business logic inside of it without doing some real work, you don't want to do that work, so you do things the right way and put your business logic in your views.  Another example would be database queries, in Django it would be harder to write a query that injected unescaped into your SQL than it would be do the right thing at use parameterized queries.

Ultimately, this is why I like Python.  The belief that best practices shouldn't be optional, and that they shouldn't be difficult creates a community where you actively want to go and learn from people's code.  Newcomers to the language aren't encouraged to "just get something working, and then clean it up later," the communiity encourages them to do it right in the first place, and save themselves the time later.

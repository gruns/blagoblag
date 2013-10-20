
When Django Fails? (A response)
===============================


I saw `an article <http://zef.me/2308/when-rails-fails>`_ on reddit (or was in hacker news?) that asked the question: what happens when newbies make typos following the Rails tutorial, and how good of a job does Rails do at giving useful error messages?  I decided it would be interesting to apply this same question to Django, and see what the results are.  I didn't have the time to review the entire Django tutorial, so instead I'm going to make the same mistakes the author of that article did and see what the results are, I've only done the first few where the analogs in Django were clear.

Mistake #1: Point a URL at a non-existent view:

I pointed a URL at the view "django_fails.views.homme" when it should have been "home".  Let's see what the error is:

.. sourcecode:: python
    
        ViewDoesNotExist at /
        Tried homme in module django_fails.views. Error was: 'module' object has no attribute 'homme'

So the exception name is definitely a good start, combined with the error text I think it's pretty clear that the view doesn't exist.

Mistake #2: misspell url in the mapping file

Instead of doing url("^$" ...) I did urll:

.. sourcecode:: python
    
        NameError at /
        name 'urll' is not defined

The error is a normal Python exception, which for a Python programmer is probably decently helpful, the cake is that if you look at the traceback it points to the exact line, in user code, that has the typo, which is exactly what you need.

Mistake #3: Linking to non-existent pages

I created a template and tried to use the {% url %} tag on a nonexistent view.

.. sourcecode:: python
    
        TemplateSyntaxError at /
        Caught an exception while rendering: Reverse for 'homme' with arguments '()' and keyword arguments '{}' not found.

It points me at the exact line of the template that's giving me the error and it says that the reverse wasn't found, it seems pretty clear to me, but it's been a while since I was new, so perhaps a new users perspective on an error like this would be important.


It seems clear to me that Django does a pretty good job with providing useful exceptions, in particular the tracebacks on template specific exceptions can show you where in your templates the errors are.  One issue I'll note that I've experience in my own work is that when you have an exception from within a templatetag it's hard to get the Python level traceback, which is important when you are debugging your own templatetags.  However, there's a ticket that's been filed for that in Django's trac.


Towards a Better Template Tag Definition Syntax
===============================================

:tags: django, python, template

`Eric Holscher <http://ericholscher.com/>`_ has blogged a `few <http://ericholscher.com/blog/2009/nov/3/class-based-template-tags/>`_ `times <http://ericholscher.com/blog/2009/nov/3/making-template-parsing-easier/>`_ this month about various template tag definition syntax ideas.  In particular he's looked at a system based on `Surlex <http://github.com/codysoyland/surlex>`_ (which is essentially an alternate syntax for certain parts of regular expressions), and a system based on keywords.  I highly recommend giving his posts a read as they explain the ideas he's looked at in far better detail than I could.  However, I wasn't particularly satisfied with either of these solution, I love Django's use of regular expressions for URL resolving, however, for whatever reason I don't really like the look of using regular expressions (or an alternate syntax like Surlex) for template tag parsing.  Instead I've been thinking about an object based parsing syntax, similar to `PyParsing <http://pyparsing.wikispaces.com/>`_.

This is an idea I've been thinking about for several months now, but Eric's posts finally gave me the kick in the pants I needed to do the work.  Therefore, I'm pleased to announce that I've released `django-kickass-templatetags <http://github.com/alex/django-templatetag-sugar>`_.  Yes, I'm looking for a better name, it's already been pointed out to me that a name like that won't fly in the US government, or most corporate environments.  This library is essentially me putting to code everything I've been thinking about, but enough talking let's take a look at what the template tag definition syntax:

.. sourcecode:: python
    
        @tag(register, [Constant("for"), Variable(), Optional([Constant("as"), Name()])]):
        def example_tag(context, val, asvar=None):

As you can see it's a purely object based syntax, with different classes for different components of a template tag.  For example this would parse something like:

.. sourcecode:: html+django
    
        {% example_tag for variable %}
        {% example_tag for variable as new_var %}

It's probably clear that this is significantly less code than the manual parsing, manual node construction, and manual resolving of variable that you would have needed to do with a raw templatetag definition.  Then the function you have gets the resolved values for each of its parameters, and at that point it's basically the same as Node.render, it is expected to either return a string to be inserted into the template or alter the context.  I'm looking forward to never writing manual template parsing again.  However, there are still a few scenarios it doens't handle, it won't handle something like the logic in the {% if %} tag, and it won't handle tags with {% end %} type tags.  I feel like these should both be solvable problems, but since it's a bolt-on addition to the existing tools it ultimately doesn't have to cover every use case, just the common ones (when's the last time you wrote your own implementation of the {% if %} or {% for %} tags).

It's my hope that something like this becomes popular, as a) developers will be happier, b) moving towards a community standard is the first step towards including a solution out of the box.  The pain and boilerplate of defining templatetags has long been a complain about Django's template language (especially because the language itself limits your ability to perform any sort of advanced logic), therefore making it as painless as possible ultimately helps make the case for the philosophy of the language itself (which I very much agree with it).

In keeping with my promise I'm giving an overview of what my next post will be, and this time I'm giving a full 3-day forecast :).  Tommorow I'm going to blog about pip, virtualenv, and my development workflow.  Sunday's post will cover a new optimization that just landed in Unladen Swallow.  And finally Monday's post will contain a strange metaphor, and I'm not saying any more :P.  `Go checkout the code and enjoy. <http://github.com/alex/django-templatetag-sugar>`_

Edit: Since this article was published the name of the library was changed to be: django-templatetag-sugar.  I've updated all the links in this post.

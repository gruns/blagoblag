
Designer Developer Relations 
=============================

:tags: design, django, html

Lately I've been working with quite a few designers so I've been thinking about what exactly constitutes the ideal working relationship.  Here are some of the models I've seen, in order of best to worst.

Best
----

The ideal relationship would be I write a view function, let the designer know what template they need to write, and what context is available, then they can ask me if they need any extra logic stuff available.  At the end I can go and add in whatever Javascript is needed.  This requires the designer to know the template language, and ideally be able to at least read model definitions so they know what properties are available to them.

Good
----

The designer provides a final templates (in the template syntax, with inheritance, blocks, etc.), with example data, and I plug some template syntax in there to wire it up with the real data.  This is pretty convenient, the one downside is that I, the developer, have to know things like "do we truncate the values here", "do we need an ellipsis", or "if we only have 4 values do we have 2 columns with 3 and 1 values, or 2 columns with 2 and 2 values".  This model requires whatever HTML/CSS the designer provides to cover all the scenarios, or the developer would be running back and forth asking questions all day.

Ok
--

The designer provides some HTML/CSS files.  For these I have to convert them to the template syntax, and substitute the real values here.  Here I need to know a lot about the semantics of the table to figure out what belongs in what blocks, how page elements are used across different pages, etc.  For this reason it's not ideal, but it can work, and it requires minimal knowledge about the programming language and tools used on the part of your designers.

Bad
---

Anything that involves me writing HTML or CSS.  I'm bad at those.


These are the working relationships I've worked with so far, the common theme is that the more your designer knows about your tools and languages the better (HTML is good, Django templates is better, being able to actually read a model definition is best).


And now for the disclaimer
==========================

:tags: disclaimer, django, internals, python

I've been discussing portions of how the Django internals work, and this is powerful knowledge for a Django user.  However, it's also internals, and unless they are documented internals are not guaranteed to continue to work.  That doesn't mean they break very frequently, they don't, but you should be aware that it has no guarantee of compatibility going forward.

Having said that, I've already discussed ways you can use this to do powerful things by using these, and you've probably seen other ways to use these in your own code.  In my development I don't really balk at the idea of using the internals, because I track Django's development very aggressively, and I can update my code as necessary, but for a lot of developers that isn't really an options.  Once you deploy something you need it to work, so your options are to either lock your code at a specific version of Django, or not using these internals.  What happens if you want to update to Django 1.1 for aggregation support, but 1.1 also removed some internal helper function you were using.  Something similar to this happened to django-tagging, before the queryset-refactor branch was merged into trunk there was a helper function to parse portions of the query, and django-tagging made use of this.  However, queryset-refactor obsoleted this function and removed, and so django-tagging had to update in order to work going forward, needing to either handle this situation in the code itself, or to maintain two separate branches.

In my opinion, while these things may break, they are worth using if you need them, because they let you do very powerful things.  This may not be the answer for everyone though.  In any event I'm going to continue writing about them, and if they interest you Marty Alchin has a book coming out, named `Pro Django <http://prodjango.com/>`_, that looks like it will cover a lot of these.

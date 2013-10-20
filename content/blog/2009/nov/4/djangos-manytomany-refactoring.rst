
Django's ManyToMany Refactoring
===============================

:tags: django, gsoc, internals, models, orm, python

If you follow Django's development, or caught next week's DjangoDose Tracking Trunk episode (what?  that's not how time flows you say?  too bad) you've seen the recent ManyToManyField refactoring that Russell Keith-Magee committed.  This refactoring was one of the results of my work as a Google Summer of Code student this summer.  The aim of that work was to bring multiple database support to Django's ORM, however, along the way I ran into refactor the way ManyToManyField's were handled, the exact changes I made are the subject of tonight's post.

If you've looked at django.db.models.fields.related you may have come away asking how code that messy could possibly underlie Django's amazing API for handling related objects, indeed the mess so is so bad that there's a comment which says:

.. sourcecode:: python
    
        # HACK

which applies to an entire class.  However, one of the real travesties of this module was that it contained a large swath of raw SQL in the manager for ManyToMany relations, for example the clear() method's implementation looks like:

.. sourcecode:: python
    
        cursor = connection.cursor()
        cursor.execute("DELETE FROM %s WHERE %s = %%s" % \
            (self.join_table, source_col_name),
            [self._pk_val])
        transaction.commit_unless_managed()

As you can see this hits the trifecta, raw SQL, manual transaction handling, and the use of a global connection object.  From my perspective the last of these was the biggest issue.  One of the tasks in my multiple database branch was to remove all uses of the global connection object, and since this uses it it was a major target for refactoring.  However, I really didn't want to rewrite any of the connection logic I'd already implemented in QuerySets.  This desire to avoid any new code duplication, coupled with a desire to remove the existing duplication (and flat out ugliness), led me to the simple solution: use the existing machinery.

Since Django 1.0 developers have been able to use a full on model for the intermediary table of a ManyToMany relation, thanks to the work of Eric Florenzano and Russell Keith-Magee.  However, that support was only used when the user explicitly provided a through model.  This of course leads to a lot of methods that basically have two implementation: one for the through model provided case, and one for the normal case -- which is yet another case of code bloat that I was now looking to eliminate.  After reviewing these items my conclusion was that the best course was to use the provided intermediary model if it was there, otherwise create a full fledged model with the same fields (and everything else) as the table that would normally be specially created for the ManyToManyField.

The end result was dynamic class generation for the intermediary model, and simple QuerySet methods for the methods on the Manager, for example the clear() method I showed earlier now looks like this:

.. sourcecode:: python
    
        self.through._default_manager.filter(**{
            source_field_name: self._pk_val
        }).delete()

Short, simple, and totally readable to anyone with familiarity with Python and Django.  In addition this move allowed Russell to fix another ticket with just two lines of code.  All in all this switch made for cleaner, smaller code and fewer bugs.

Tomorrow I'm going to be writing about both the talk I'm going to be giving at PyCon, as well as my experience as a member of the PyCon program committee.  See you then.

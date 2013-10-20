
What I'm excited about in Django 1.1
====================================


This past week, Jacob Kaplan-Moss put together the list of all of the features proposed for Django 1.1, and began to solicit comments on them.  This is going to be a list of features I'm excited about.
 * Making admin URLs reversable.  Currently the Django Admin uses a bit of a convulted scheme to route URLs.  The proposal is to have them work using the current URL scheme.  This is something I've been working on for a while, and hoping to see it to completion.
 * Comment-utils inclusion.  The proposal is to include the moderation level features from comment-utils in Django.  I think this is a great idea, and can't wait to see what sort of spam check schemes people implement once moderation facilities are included.
 * Message passing for anonymous users.  This is basically session level message passing.  This is something I've had to implement in past, so I'm looking forward to this.
 * ORM aggregation, as part of the Google Summer of Code Nicolas Lara, mentored by Russell Keith-Magee, implemented this.  I love the API design, and it's a hugely requested feature, I can't wait to point new users to the docs, rather than explaining to them that it's coming soon.
 * ORM expression support, this work was also done by Nicolas Lara, and will let you do things like Model.objects.filter(height__gt=F('width')), or Model.objects.update(salary = F('salary')*1.2).
 * Model Validation, before 1.0 I implemented unique, and unique_together checks for model forms.  That's pretty much a massive special case of this.
 * Class-based generic views, often one of the first things a new user to Django will learn to do is create a view that simply wraps a generic view, in order to do some custom filtering on a queryset.  This is a great solution for that usecase, however as users want to inject more and more flexibility into a generic view it can lead to a huge number of settings.  Rather than this, subclassing a generic view could provide a nice clean solution.

These will all be great features, and there are many more proposed(you can see them all `here <http://spreadsheets.google.com/ccc?key=pSqnCvef6OXmGWQ9qbEVMeA>`_), however these features only happen because people write code for them.  If there's a feature you're excited about, or interested in making a reality, try to contribute to it, even if it's just writing some unit tests.

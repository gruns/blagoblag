
Committer Models of Unladen Swallow, PyPy, and Django 
======================================================


During this year's PyCon I became a committer on both PyPy and Unladen Swallow, in addition I've been a contributer to Django for quite a long time (as well as having commit privileges to my branch during the Google Summer of Code).  One of the things I've observed is the very different models these projects have for granting commit privileges, and what the expectations and responsibilities are for committers.

Unladen Swallow
---------------

Unladen Swallow is a Google funded branch of CPython focused on speed.  One of the things I've found is that the developers of this project carry over some of the development process from Google, specifically doing code review on every patch.  All patches are posted to `Rietveld <http://codereview.appspot.com>`_, and reviewed, often by multiple people in the case of large patches, before being committed.  Because there is a high level of review it is possible to grant commit privileges to people without requiring perfection in their patches, as long as they follow the review process the project is well insulated against a bad patch.

PyPy
----

PyPy is also an implementation of Python, however its development model is based largely around aggressive branching (I've never seen a project handle SVN's branching failures as well as PyPy) as well as sprints and pair programming.  By branching aggressively PyPy avoids the overhead of reviewing every single patch, and instead only requires review when something is already believed to be "trunk-ready", further this model encourages experimentation (in the same way git's light weight branches do).  PyPy's use of sprints and pair programming are two ways to avoid formal code reviews and instead approach code quality as more of a collaborative effort.

Django
------

Django is the project I've been involved with for the longest, and also the only one I don't have commit privileges on.  Django is extremely conservative in giving out commit privileges (there about a dozen Django committers, and about 500 names in the AUTHORS file).  Django's development model is based neither on branching (only changes as large in scope as multiple database support, or an admin UI refactor get their own branch) nor on code review (most commits are reviewed by no one besides the person who commits them).  Django's committers maintain a level of autonomy that isn't seen in either of the other two projects.  This fact comes from the period before Django 1.0 was released when Django's trunk was often used in production, and the need to keep it stable at all times, combined with the fact that Django has no paid developers who can guarantee time to do code review on patches.  Therefore Django has maintained code quality by being extremely conservative in granting commit privileges and allowing developers with commit privileges to exercise their own judgment at all times.

Conclusion
----------

Each of these projects uses different methods for maintaining code quality, and all seem to be successful in doing so.  It's not clear whether there's any one model that's better than the others, or that any of these projects could work with another's model.  Lastly, it's worth noting that all of these models are fairly orthogonal to the centralized VCS vs. DVCS debate which often surrounds such discussions.

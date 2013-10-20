
Effective Code Review
=====================


Maybe you practice code review, either as a part of your open source project or
as a part of your team at work, maybe you don't yet. But if you're working on a
software project with more than one person it is, in my view, a necessary piece
of a healthy workflow. The purpose of this piece is to try to convince you its
valuable, and show you how to do it effectively.

This is based on my experience doing code review both as a part of my job at
several different companies, as well as in various open source projects.

What
----

It seems only seems fair that before I try to convince you to make code review
an integral part of your workflow, I precisely define what it is.

Code review is the process of having another human being read over a diff. It's
exactly like what you might do to review someone's blog post or essay, except
it's applied to code. It's important to note that code review is about
**code**. Code review doesn't mean an architecture review, a system design
review, or anything like that.

Why
---

Why should you do code review? It's got a few benefits:

* It raises the `bus factor`_. By forcing someone else to have the familiarity
  to review a piece of code you guarantee that at least two people understand
  it.
* It ensures readability. By getting someone else to provide feedback based on
  *reading*, rather than *writing*, the code you verify that the code is
  readable, and give an opportunity for someone with fresh eyes to suggest
  improvements.
* It catches bugs. By getting more eyes on a piece of code, you increase the
  chances that someone will notice a bug before it manifests itself in
  production. This is in keeping with Eric Raymond's maxim that, "given enough
  eyeballs, all bugs are shallow".
* It encourages a healthy engineering culture. Feedback is important for
  engineers to grow in their jobs. By having a culture of "everyone's code gets
  reviewed" you promote a culture of positive, constructive feedback. In teams
  without review processes, or where reviews are infrequent, code review tends
  to be a tool for criticism, rather than learning and growth.

How
---

So now that I've, hopefully, convinced you to make code review a part of your
workflow how do you put it into practice?

First, a few ground rules:

* Don't use humans to check for things a machine can. This means that code
  review **isn't** a process of running your tests, or looking for style guide
  violations. Get a CI server to check for those, and have it run
  automatically. This is for two reasons: first, if a human has to do it,
  they'll do it wrong (this is true of everything), second, people respond to
  certain types of reviews better when they come from a machine. If I leave the
  review "this line is longer than our style guide suggests" I'm nitpicking and
  being a pain in the ass, if a computer leaves that review, it's just doing
  it's job.
* Everybody gets code reviewed. Code review isn't something senior engineers do
  to junior engineers, it's something everyone participates in. Code review can
  be a great equalizer, senior engineers shouldn't have special privledges, and
  their code certainly isn't above the review of others.
* Do pre-commit code review. Some teams do post-commit code review, where a
  change is reviewed after it's already pushed to ``master``. This is a bad
  idea. Reviewing a commit after it's already been landed promotes a feeling of
  inevitability or fait accompli, reviewers tend to focus less on small details
  (even when they're important!) because they don't want to be seen as causing
  problems after a change is landed.
* All patches get code reviewed. Code review applies to all changes for the
  same reasons as you run your tests for all changes. People are really bad at
  guessing the implications of "small patches" (there's a near 100% rate of me
  breaking the build on change that are "so small, I don't need to run the
  tests"). It also encourages you to have a system that makes code review easy,
  you're going to be using it a lot! Finally, having a strict "everything gets
  code reviewed" policy helps you avoid arguments about just how small is a
  small patch.

So how do you start? First, get yourself a system. `Phabricator`_,
`Github's pull requests`_, and `Gerrit`_ are the three systems I've used, any
of them will work fine. The major benefit of having a tool (over just mailing
patches around) is that it'll keep track of the history of reviews, and will
let you easily do commenting on a line-by-line basis.

You can either have patch authors land their changes once they're approved, or
you can have the reviewer merge a change once it's approved. Either system
works fine.

**As a patch author**

Patch authors only have a few responsibilities (besides writing the patch
itself!).

First, they need to express what the patch does, and why, clearly.

Second, they need to keep their changes small. Studies have shown that beyond
200-400 lines of diff, patch review efficacy trails off [#]_. You want to keep
your patches small so they can be effectively reviewed.

It's also important to remember that code review is a collaborative feedback
process if you disagree with a review note you should start a conversation
about it, don't just ignore it, or implement it even though you disagree.

**As a review**

As a patch reviewer, you're going to be looking for a few things, I recommend
reviewing for these attributes in this order:

* Intent - What change is the patch author trying to make, is the bug they're
  fixing really a bug? Is the feature they're adding one we want?
* Architecture - Are they making the change in the right place? Did they change
  the HTML when really the CSS was busted?
* Implementation - Does the patch do what it says? Is it possibly introducing
  new bugs? Does it have documentation and tests? This is the nitty-gritty of
  code review.
* Grammar - The little things. Does this variable need a better name? Should
  that be a keyword argument?

You're going to want to start at intent and work your way down. The reason for
this is that if you start giving feedback on variable names, and other small
details (which are the easiest to notice), you're going to be less likely to
notice that the entire patch is in the wrong place! Or that you didn't want the
patch in the first place!

Doing reviews on concepts and architecture is *harder* than reviewing
individual lines of code, that's why it's important to force yourself to start
there.

There are three different types of review elements:

* TODOs: These are things which must be addressed before the patch can be
  landed; for example a bug in the code, or a regression.
* Questions: These are things which must be addressed, but don't necessarily
  require any changes; for example, "Doesn't this class already exist in the
  stdlib?"
* Suggestions for follow up: Sometimes you'll want to suggest a change, but
  it's big, or not strictly related to the current patch, and can be done
  separately. You should still mention these as a part of a review in case the
  author wants to adjust anything as a result.

It's important to note which type of feedback each comment you leave is (if
it's not already obvious).

Conclusion
----------

Code review is an important part of a healthy engineering culture and workflow.
Hopefully, this post has given you an idea of either how to implement it for
your team, or how to improve your existing workflow.


.. _`bus factor`: https://en.wikipedia.org/wiki/Bus_factor
.. _`Phabricator`: http://phabricator.org/
.. _`Github's pull requests`: https://help.github.com/articles/using-pull-requests#reviewing-proposed-changes
.. _`Gerrit`: https://code.google.com/p/gerrit/

.. [#] http://www.ibm.com/developerworks/rational/library/11-proven-practices-for-peer-review/

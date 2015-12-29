Shrinking your code review
==========================

It's an unfortunate reality, but one of the few things we know about software
quality is that lines of code is positive correlated with bugs, or as Notorious
B.I.G. would say, "Mo Code Mo Problems". Code review faces a similar challenge:
the larger a patch you're reviewing, the less effective your code review is [#]_.

There's a few reasons for this:

* The more code you're changing, the more you need to focus on the big picture.
  If you're changing your database tables, your business logic, and your
  presentation layer you need to focus on the overall architecture, making sure
  everything is in the correct place. It's hard to focus on the little details
  (like: does the business logic even do the right thing) when you're looking
  at the big picture.
* It encourages bikeshedding. Ironically, in addition to making it harder to
  focus on details, the large scope of a large patch means that fewer people
  feel capable of providing substantive feedback, this encourages low quality
  feedback on unimportant minutia.
* You duplicate work (or skip it). If a patch goes through a few iterations,
  it's not uncommon for the majority of changes between iterations to be in one
  part of the patch. If you have a large patch the surface area of code which
  doesn't change between iterations will also be large. The result is that
  either you have to review it over and over again (taking time away from the
  more "exciting" part of the review) or you just skim over it, providing a
  less thorough review. Code like this ends up being held to a different
  standard than if it were reviewed by itself.

In short, it's hard to focus your attention on what's important when there's a
lot going on. Or as one developer succinctly put it:

.. raw:: html

    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">10 lines of code = 10 issues.&#10;&#10;500 lines of code = &quot;looks fine.&quot;&#10;&#10;Code reviews.</p>&mdash; I Am Devloper (@iamdevloper) <a href="https://twitter.com/iamdevloper/status/397664295875805184">November 5, 2013</a></blockquote>
    <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

How do we solve this? Smart ass answer: smaller code reviews! Ok but *how*?

Fundamentally there's only two ways to get smaller reviews: write less code or
split your changes up across multiple reviews. I'm not going to focus on
writing less code, a great much about has been written about this topic.
Instead I'm going to focus on how to split up your changes.

I want to start with a meta point: don't try to prematurely split up your
patch. Write your feature or bugfix as you normally would, file a pull request
with everything in one patch, and then work with your reviewers to split the
patch up.

With that out of the way, here's a few tactics for splitting up a large patch:

**Dependencies**: If your patch upgrades a dependency, split that out. Often
you'll bump a dependency and then go to resolve a deprecation warning or add a
new feature using it. Do the bump in a separate PR. This is particularly
important if you vendor your dependencies, where changes to the vendored files
will "pollute" review space, making it easy to miss the changes to your
software.

**Utilities**: If your patch adds stand-alone utility functions, split them
out. These are often the easiest thing to break out, particularly pure
functions which can be easily unit tested.

**Functionality**: If your patch adds functionality that spans several layers
of your application, say a new feature for a webapp, which contains a new
database table and accompanying business logic, controller methods, forms, and
HTML, split the different pieces apart. First land the new database tables and
migrations, then the business logic and accompany tests, then the forms,
controllers, and HTML. For patches like this it's particularly important to
post the "complete" patch before breaking it apart so reviewers have a bit of
context what you're driving towards. If the scope of your feature is
particularly large, you'll likely want to explore `feature flags`_ as a
mechanism for allowing pieces to be landed individually without needing to be
launch-ready.

**Refactors**: A common pattern is to start writing a feature (or a bugfix) and
realize the code is a bit messy and to end up with both some cleanups or
refactors and the feature you originally set out to write. Split that refactor
out.

In the process of splitting a patch out, you may have to write small amounts of
code that are specific to the intermediate state (for example, a test that a
particularly code path *isn't* implemented yet). Each pull request that's
merged should stand alone, tests that assert that the intermediate state is
correct are just as important as ones that assert about the final state.

One final note: to do this in practice, it's important you know your VCS well.
``git`` in particular has many features which make this type of workflow
pleasant if you know them well.

.. [#] https://smartbear.com/SmartBear/media/pdfs/11_Best_Practices_for_Peer_Code_Review.pdf

.. _`feature flags`: https://blog.travis-ci.com/2014-03-04-use-feature-flags-to-ship-changes-with-confidence/


You guys know who Philo Farnsworth was?
=======================================


Friends of mine will know I'm a very big fan of the TV show `Sports Night`_
(really any of Aaron Sorkin's writing, but Sports Night in particular). Before
you read anything I have to say, take a couple of minutes and watch this clip:

.. raw:: html

    <iframe width="480" height="360" src="//www.youtube.com/embed/H-va0tWJLTc" frameborder="0" allowfullscreen></iframe>

I doubt Sorkin knew it when he scripted this (I doubt he knows it now either),
but this piece is about how Open Source happens (to be honest, I doubt he knows
what Open Source Software is).

This short clip actually makes two profound observations about open source.

First, most contribution are not big things. They're not adding huge new
features, they're not rearchitecting the whole system to address some
limitation, they're not even fixing a super annoying bug that affects every
single user. Nope, most of them are adding a missing sentence to the docs,
fixing a bug in a wacky edge case, or adding a tiny hook so the software is a
bit more flexible. And this is fantastic.

The common wisdom says that the thing open source is really bad at is polish.
My experience has been the opposite, no one is better at finding increasingly
edge case bugs than open source users. And no one is better at fixing edge case
bugs than open source contributors (who overlap very nicely with open source
users).

The second lesson in that clip is about how to be an effective contributor.
Specifically that one of the keys to getting involved effectively is for other
people to recognize that you know how to do things (this is an empirical
observation, not a claim of how things ought to be). How can you do that?

* Write good bug reports. Don't just say "it doesn't work", if you've been a
  programmer for any length of time, you know this isn't a useful bug report.
  What doesn't work? Show us the traceback, or otherwise unexpected behavior,
  include a test case or instructions for reproduction.
* Don't skimp on the details. When you're writing a patch, make sure you
  include docs, tests, and follow the style guide, don't just throw up the
  laziest work possible. Attention to detail (or lack thereof) communicates
  very clearly to someone reviewing your work.
* Start a dialogue. Before you send that 2,000 line patch with that big new
  feature, check in on the mailing list. Make sure you're working in a way
  that's compatible with where the project is headed, give people a chance to
  give you some feedback on the new APIs you're introducing.

This all works in reverse too, projects need to treat contributors with
respect, and show them that the project is worth their time:

* Follow community standards. In Python this means things like `PEP8`_, having
  a working ``setup.py``, and using `Sphinx`_ for documentation.
* Have passing tests. Nothing throws me for a loop worse than when I checkout a
  project to contribute and the tests don't pass.
* Automate things. Things like running your tests, linters, even state changes
  in the ticket tracker should all be automated. The alternative is making
  human beings manually do a bunch of "machine work", which will often be
  forgotten, leading to a sub-par experience for everyone.


.. raw:: html

    <p>Remember, <span style="text-decoration: line-through;">Soylent Green</span> Open Source is people</p>

That's it, the blog post's over.


.. _`Sports Night`: https://en.wikipedia.org/wiki/Sports_Night
.. _`PEP8`: http://www.python.org/dev/peps/pep-0008/
.. _`Sphinx`: http://sphinx-doc.org/

About Python 3
==============

Python community, friends, fellow developers, we need to talk. On December 3rd,
2008 Python 3.0 was first released. At the time it was widely said that Python
3 adoption was going to be a long process, it was referred to as a five year
process. We've just passed the five year mark.

At the time of Python 3's release, and for years afterwards I was very excited
about it, evangelizing it, porting my projects to it, for the past year or two
every new projects I've started has had Python 3 support from the get go.

Over the past six months or so, I've been reconsidering this position, and
excitement has given way to despair.

For the first few years of the Python 3 migration, the common wisdom was that
a few open source projects would need to migrate, and then the flood gates
would open. In the Django world, that meant we needed a WSGI specification, we
needed database drivers to migrate, and then we could migrate, and then our
users could migrate.

By now, all that has happened, Django (and much of the app ecosystem) now
supports Python 3, NumPy and the scientific ecosystem supports Python 3,
several new releases of Python itself have been released, and users still
aren't using it.

Looking at download statistics for the Python Package Index, we can see that
Python 3 represents under 2% of package downloads. Worse still, almost no code
is written for Python 3. As I said all of my new code supports Python 3, but I
run it locally with Python 2, I test it locally with Python 2; Travis CI runs
it under Python 3 for me; certainly none of my code is Python 3 only. At
companies with large Python code bases I talk to no one is writing Python 3
code, and basically none of them are thinking about migrating their codebases
to Python 3.

Since the time of the Python 3.1 it's been regularly said that the new features
and additions the standard library would act as carrots to motivate people to
upgrade. Don't get me wrong, Python 3.3 has some really cool stuff in it. But
99% of everybody can't actually use it, so when we tell them "that's better in
Python 3", we're really telling them "Fuck You", because nothing is getting
fixed for them.

Beyond all of this, it has a nasty pernicious effect on the development of
Python itself: it means there's no feedback cycle. The fact that Python 3 is
being exclusively by very early adopters means that what little feedback
happens on new features comes from users who may not be totally representative
of the broader community. And as we get farther and farther in the 3.X series
it gets worse and worse. Now we're building features on top of other features
and at no level have they been subjected to actual wide usage.

Why aren't people using Python 3?
---------------------------------

First, I think it's because of a lack of urgency. Many years ago, before I knew
how to program, the decision to have Python 3 releases live in parallel to
Python 2 releases was made. In retrospect this was a mistake, it resulted in a
complete lack of urgency for the community to move, and the lack of urgency has
given way to lethargy.

Second, I think there's been little uptake because Python 3 is fundamentally
unexciting. It doesn't have the super big ticket items people want, such as
removal of the GIL or better performance (for which many are using PyPy).
Instead it has many new libraries (whose need is largely filled by
``pip install``), and small cleanups which many experienced Python developers
just avoid by habit at this point. Certainly nothing that would make one stop
their development for any length of time to upgrade, not when Python 2 seems
like it's going to be here for a while.

So where does this leave us?
----------------------------

Not a happy place. First and foremost I think a lot of us need to be more
realistic about the state of Python 3. Particularly the fact that for the last
few years, for the average developer Python, the language, has not gotten
better.

The divergent paths of Python 2 and Python 3 have been bad for our community.
We need to bring them back together.

Here's an idea: let's release a Python 2.8 which backports every new feature
from Python 3. It will also deprecate anything which can't be changed in a
backwards compatible fashion, for example ``str + unicode`` will emit a
warning, as will any file which doesn't have
``from __future__ import unicode_literals``. Users need to be able to follow a
continuous process for their upgrades, Python 3 broke it, let's fix it.

That's my only idea. We need more ideas. We need to bridge this gap, because
with every Python 3 release, it grows wider.

*Thanks to Maciej Fijalkowski and several others for their reviews, it goes
without saying that all remaining errors are my own.*


Priorities
==========


When you work on something as large and multi-faceted as Django you need a way to prioritize what you work on, without a system how do I decide if I should work on a new feature for the template system, a bugfix in the ORM, a performance improvement to the localization features, or better docs for ``contrib.auth``?  There's tons of places to jump in and work on something in Django, and if you aren't a committer you'll eventually need one to commit your work to Django.  So if you ever need me to commit something, here's how I prioritize my time on Django:

    1) **Things I broke**: If I broke a buildbot, or there's a ticket reported against something I committed this is my #1 priority.  Though Django no longer has a policy of trunk generally being perfectly stable it's still a very good way to treat it, once it gets out of shape it's hard to get it back into good standing.
    2) **Things I need for work**: Strictly speaking these don't compete with the other items on this list, in that these happen on my work's time, rather than in my free time.  However, practically speaking, this makes them a relatively high priority, since my work time is fixed, as opposed to free time for Django, which is rather elastic.
    3) **Things that take me almost no time**: These are mostly things like typos in the documentation, or really tiny bugfixes.
    4) **Things I think are cool or important**: These are either things I personally think are fun to work on, or are in high demand from the community.
    5) **Other things brought to my attention**: This is the most important category, I can only work on bugs or features that I know exist.  Django's trac has about 2000 tickets, way too many for me to ever sift through in one sitting.  Therefore, if you want me to take a look at a bug or a proposed patch it needs to be brought to my attention.  Just pinging me on IRC is enough, if I have the time I'm almost always willing to take a look.

In actuality the vast majority of my time is spent in the bottom half of this list, it's pretty rare for the build to be broken, and even rarer for me to need something for work, however, there are tons of small things, and even more cool things to work on.  An important thing to remember is that the best way to make something show up in category #3 is to have an awesome patch with tests and documentation, if all I need to do is ``git apply && git commit`` that saves me a ton of time.

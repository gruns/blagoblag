
Announcing VCS Translator
=========================


For the past month or so I've been using a combination of Google, Stackoverflow, and bugging people on IRC to muddle my way through using various VCS that I'm not very familiar with.  And all too often my queries are of the form of "how do I do git foobar -q in mercurial?".  A while ago I tweeted that someone should write a VCS translator website.  Nobody else did, so when I woke up far too early today I decided I was going to get something online to solve this problem, today!  About 6 hours later `I tweeted <http://twitter.com/#!/alex_gaynor/status/28514110215815168>`_ the launch of `VCS translator <http://vcs-translator.ep.io/>`_.

This is probably not even a minimum viable product.  It doesn't handle a huge range of cases, or version control systems.  However, it is open source and it provides a framework for answering these questions.  If you're interested I'd encourage you to fork it `on github <https://github.com/alex/vcs-translator>`_ and help me out in fixing some of the `most requested translation <http://vcs-translator.ep.io/help/>`_ (I remove them once they're implemented).

My future goals for this are to allow commenting, so users can explain the caveats of the translations (very infrequently are the translations one-to-one) and to add a proper API.  Moreover my goal is to make this a useful tool to other programmers who, like myself, have far too many VCS in their lives.

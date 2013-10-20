
PyPy San Francisco Tour Recap
=============================


Yesterday was the last day of my (our) tour of the Bay Area, so I figured I'd post a recap of all the cool stuff that happened.

Sprints
-------

I got in on Friday night (technically Saturday morning, thanks for the ride Noah!) and on Saturday and Sunday we held sprints at Noisebridge.  They have a very cool location and we had some pretty productive sprints.  The turnout was less than expected, based on the people who said they'd show at the Python user group, however we were pretty productive.  We fixed a number of remaining issues before we can do a Python 2.7 compatible release.  These included: Armin Rigo and I implementing ``PYTHONIOENCODING`` (look it up!), Dan Roberts fixing the ``sqlite3`` tests, and Armin fixing a subtle JIT bug.  I also spent some time doing some performance profiling with Greg from Quora.  Importing ``pytz`` was incredibly slow on PyPy, and it turned out the issue was when ``pytz`` was in a ``.egg`` its attempts to load the timezone files cause repeated reads from the ZIP file, and PyPy wasn't caching the zipfile metadata properly.  So we fixed that and now it's much faster.

Google
------

Monday morning we (Armin Rigo, Maciej Fijalkowski, and myself) gave a tech talk at Google.  The first thing I noticed was the Google campus is obscenely gorgeous, and large.  Unfortunately, our talk didn't seem to go very well.  Part of this was we were unsure if our audience was Python developers looking to make their code run faster, or compiler people who wanted to hear all the gory details of our internals.  Even now I am still a little unsure about who showed up to our talk, but they didn't seem very enthused.  I'm hoping we can construct some sort of post-mortem on the talk, because Google is precisely the type of company with a lot of Python code and performance aspirations that we think we can help with.  (And Google's cafeterias are quite delicious).

Mozilla
-------

After lunch at Google we shuffled over to Mozilla's offices for another talk.  The slides we delivered were the same as the Google ones, however this talk went over much better.  Our audience was primarily compiler people (who work on the Tracemonkey/Jaegermonkey/other Javascript engines), with a few Python developers who were interested.  We had a ton of good questions during and after the talk, and then hung around for some great discussions with Brendan Eich, Andreas Gal, David Mandelin, and Chris Leary, kudos to all those guys.  Some of the major topics were:

 * Whether or not we had issues of trace explosion (over specializing traces and thus compiling a huge number of paths that were in practice rarely executed), and why not.
 * The nature of the code we have to optimize, a good bit of real world Python is mostly idiomatic, whereas Mozilla really has to deal with a problem of making any old crap on the internet fast.
 * The fact that for Javascript script execution time is generally **very** short, whereas the Python applications we target tend to have longer execution times.  While we still work to startup quickly (e.g. no 5 minute JVM startup times), it's less of an issue if it takes 30 seconds before the code starts running at top speed.  For us this means that targeting browser Javascript is possibly less sensible than server-side Javascript for a possible Javascript VM written on top of our infrastructure.

Overall it was a very positive experience, and I'll be excited to speak with David some more at the VM summit at PyCon.

Recap
-----

Overall the trip was a big success in my view.  I believe both the Google and Mozilla talks were recorded, so once I know where they are online hopefully other people can enjoy the talks.  Hopefully Armin will blog about some of the talks he gave before I got to the Bay Area.  See you at PyCon!

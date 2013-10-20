
The Pycon Program Committee and my PyCon Talk
=============================================


Last year I presented at a conference for the first time in my life at PyCon, I moderated a panel on ORMs and I enjoyed it a ton (and based on the feedback I've gotten at least a few people enjoyed attending it).  Above and beyond that the two PyCons I've attended have both been amazing conferences, tons of awesome talks, great people to hang out with, and an awesome environment for maximizing both.  For both of the last two years I've hung around the PyCon organizers mailing list since the conference was in Chicago and I lived there, however this year I really wanted to increase my contributions to such a great conference.  Therefore, I joined the Pycon program committee.  This committee is responsible for reviewing all talk submissions and selecting the talks that will ultimately appear at PyCon.

This year the PyCon programming committee had a really gargantuan task.  There were more talks submitted then ever before, more than 170 of them, for only 90 or so slots.  Unfortunately this meant that we had to reject some really good talks, which always sucks.  There's been a fair bit of discussion about the process this year and what can be done to improve it.  As a reviewer the one thing I wish I'd known going in was that the votes left on talks were just a first round, and ultimately didn't count for a huge amount.  Had I known this I would have been less tepid in giving positive reviews to talks which merely looked interesting.

Another hot topic in the aftermath is whether or not the speaker's identity should factor into a reviewer's decision.  My position is that it should wherein the speaker has a reputation, be it good or bad.  If I know a speaker is awesome I'm way more likely to give them the +1, likewise if I see a speaker has a history of poor talks I'm more likely to give them a -1.  That being said I don't think new speakers, or slightly inexperienced ones should be penalized for that, I was a brand new speaker last time and I'm grateful I was given the chance to present.

To give an example of this one of the talks I'm really looking forward to is Mark Ramm's, "To relate or not to relate, that is the question".  Mark and I spoke about this topic for quite a while at PyOhio, and every talk from Mark I've ever seen has been excellent.  Therefore I was more than willing to +1 it.  However, had I not known the speaker it would still have been a good proposal, and an interesting topic, I just would not have gotten immediately excited about going to see the talk.

As an attendee one of the things I've always found is that speakers who are very passionate about their topics almost always give talks I really enjoy.  Thinking back to my first PyCon Maciej Fijalkowski managed to get me excited and interested in PyPy in just 30 minutes, because he was so passionate in speaking about the topic.

All that being said I wanted to share a short list of the talks I'm excited about this year, before I dive into what my own talk will be about:
 * Optimizations And Micro-Optimizations In CPython
 * Unladen Swallow: fewer coconuts, faster Python
 * Managing the world's oldest Django project
 * Understanding the Python GIL
 * The speed of PyPy
 * Teaching compilers with python
 * To relate or not to relate, that is the question
 * Modern version control: Mercurial internals
 * Eventlet: Asynchronous I/O with a synchronous interface
 * Hg and Git : Can't we all just get along?
 * Mastering Team Play: Four powerful examples of composing Python tools


It's a bit of a long list, but compared to the size of the list of accepted talks I'm sure there are quite a few gems I've missed.

The talk I'm going to be giving this year is about the real time web, also known as HTTP push, Comet, or reverse Ajax.  All of those are basically synonyms for the server being able to push data to the browser, rather than having the browser constantly poll the server for data.  Specifically I'm going to be looking at my experience building three different things, LeafyChat, DjangoDose's DjangoCon stream, and Hurricane.

Leafychat is an IRC client built for the DjangoDash by myself, Leah Culver, and Chris Wanstrath.  The DjangoDose DjangoCon stream was a live stream of all the Twitter items about DjangoCon that Eric Florenzano and I built in the week leading up to DjangoCon.  Finally, Hurricane is the library Eric Florenzano and I have been working on in order to abstract the lessons learned from our experience building "real time" applications in Python.

In the talk I'm going to try to zero in on what we did for each of these projects, what worked, what didn't, and what I'm taking away from the experience.  Finally, Eric Florenzano and I are working to put together a new updated, better version of the DjangoCon stream for PyCon.  I'm going to discuss what we do with that project, and why we do it that way in light of the lessons of previous projects.

I'm hoping both my talk, and all of them will be awesome.  One thing's for sure, I'm already looking forward to PyCon 2010.  Tomorrow I'm going to be writing about my thoughts on a more ideal template tag definition syntax for Django, and hopefully sharing some code if I have time to start working on it.  See you then (and in Atlanta ;))!


PyCon Wrapup
============

:tags: django, pycon, python

With PyCon now over for me(and the sprints just begining for those still there) I figured I'd recap it for those who couldn't be there, and compare notes for those who were.  I'll be doing a separate post to cover my panel, since I have quite a brain dump there.

Day One
-------

We start off the morning with lightning talks, much better than last year due to the removal of so many sponsor talks(thanks Jacob), by now I've already met up with quite a few Django people.  Next I move on to the "Python for CS1" talk, this was particularly interesting for me since they moved away from C++, which is exactly what my school uses.  Next, on to "Introduction to CherryPy" with a few other Djangonauts.  CherryPy looks interesting as a minimalist framework, however a lot of the callback/plugin architecture was confusing me, so I feel like I'd be ignoring it and just being very close to the metal, which isn't always a bad thing, something to explore in the future.  For there I'm off to "How Python is Developed", it's very clear that Django's development model is based of Python's, and that seems to work for both parties.

Now we head to lunch, which was fantastic, thanks to whoever put it together.  From there I go to "Panel: Python VMs", this was very informative, though I didn't have a chance to ask my question, "Eveyone on the panel has mentioned that performance is likely to improve greatly in the future as a potential reason to use their alternate VM, should Unladen Swallow succeed in their goal, how does that affect you?".  After that I went to the "Twisted, AMQP, and Thrift" talk, it was fairly good, though this feels like a space I have to look at more, or have a real world use case for, to totally understand.

A quick break, and then we're on to Jesse Noller's mutliprocessing talk.  Jesse really is the expert in this, and having used the multiprocessing library before it's clear to me there's still tons of cool stuff to explore.  Lastly we had the "Behind the scenes of Everyblock.com" from Adrian, it's very cool to see their architecture and it's getting me excited for their going open source in June.  I also got a bit out a shoutout here when Adrian was asked about future scalability and he mentioned sharding across multiple databases.  We had lightning talks and that was the end of the official conference for the day.

In the evening a big group of us(officially a Pinax meetup, but I think we had more than that) went to a restaurant, as the evening progressed our group shrunk, until they finally kicked us out at closing time.  A good time was had by all I think.

Day two
-------

After staying out exceptionally late the night before I ended up sleeping on the floor with friends rather than heading home(thanks!) so, retrospectively, day two should have been tiring, but it was as high energy as could be.  I began the morning with lightning talks followed by Guido's keynote, which was a little odd and jumped around a lot, but I found I really enjoyed it.  After that I got to sit in one room for 3 talks in a row, "The State of Django", "Pinax", and "State of TurboGears", which I can say, without qualifications, were all great(I received another shoutout during the Django talk, I guess I really need to deliver, assuming the GSOC project is accepted).  From there it was off to lunch.

After lunch it was time to take the stage for my "ORM Panel".  I'm saving all the details for another blog post, but I think it went well.  After this we had a Django Birds of a Feather session, which was very fun.  We got to see Honza Kraal show off the cool features of the Ella admin.  The highlight had to be having Jacob Kalpan-Moss rotate us around the room to get Djangonauts to meet each other.

After this I heard Jesse Noller's second concurrency talk, and then Ian Bicking's talk on ... stuff, both talks were great, but Ian's is probably in a "you had to be there" category.

After that it was time for lightning talks, followed by what was supposed to be dinner for people interested in Oebfare(Django blog application) to make some design decisions.  In the end quite a few more people were there and I got to meet some really cool people like Mark Pilgrim.  After dinner it was back to the Hyatt for about an hour of hacking on Django before I called it a night.

Day Three
---------

The final day of the conference.  Once again I began my day with some lightning talks.  After this was the keynote, by the reddit.com creators.  They gave a short, but interesting keynote and answered a lot of questions.  I have to say that some of their technical answers were less than satisfying.  After this I went to an open space on podcasting where I learned that I'm probably the only person who doesn't mind podcasts that are over an hour long.

After this I went to the Eve Online talk, but I ended up leaving for the testing tools panel.  This panel was interesting, but I can't help but feel that the Python community would be best served by getting the testing tools that everyone agrees about into the unittest module in the Python standard library.  For my last talk of the conference I saw Jacob Kaplan-Moss's talk on "Django's design decisions", thankfully this didn't step on the toes of the ORM design decision panel, and it was very interesting.  From there it was off to lunch, and a final round of lightning talks, capped off my Guido running away with the Django Pony(I hope someone caught this on video), and my conference was done.

This was a really great conference for me, hopefully everyone else enjoyed it as much as I did.  I'll be doing a follow up post where I answer some of the questions I've seen about the ORM panel, as well as put the rest of my thoughts on paper(hard disk).  And now if you'll excuse me, I have a virtual sprint to attend.

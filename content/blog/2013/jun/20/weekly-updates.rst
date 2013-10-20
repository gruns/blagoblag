
Weekly Updates
==============

:tags: rackspace

One of the great luxuries of my new job at Rackspace is that basically everything I work on is open source, which means I also have the ability to write and talk about almost everything I do! Since a large chunk of my time is dedicated to working on open source projects of my choice, I wanted to start writing regularly about what I'm doing with that time. To that end I'm going to try to write regularly (hopefully every Monday) about my goals for the week. Since today is a Thursday, I'll tell you about what I've done thus far this week:

* I spent Monday meeting with some folks at Oracle Research, to talk about PyPy, JITs, and other fun optimization stuff. Once their papers are public I'll link to them, for now you can find some information at http://openjdk.java.net/projects/graal/
* I started working on improving the multi-datacenter support for Rackspace in libcloud. I added support for the Sydney data center in the compute and object-storage drivers, and I'm working on refactoring the DNS and load balancer drivers to better support multiple datacenters (right now you have one class per datacenter, which sucks)
* I added some features and fixed some bugs in Topaz (mostly I just broke the build a ton of times, please don't look at the travis-ci history, it's embarrassing).
* I've been working on my slides for my DjangoCon.AU and PyCon AU keynotes.

And that's been my week!

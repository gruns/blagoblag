DevOps vs. Platform Engineering
===============================

If I put 10 people in a room and asked them what "DevOps" was all about, I
think I'd get 17 different answers. As my colleague David Reid says though,
"DevOps is something you do, not something you are." So what practices are
assosciated with DevOps?

* Using software to automate operations tasks
* Using configuration management tools such as Chef and Puppet
* Treating servers as "cattle not pets"

-------

Database as a Service is to Database as Load Balancer as a Service is to Load
Balanacer as Platform as a Service is to ____________. If you answered
"platform", a) your elementary school teachers can be very proud, b) it's not
clear that you're right.

When Heroku launched, something interesting happened: they gave people a
Platform as a Service before most people had a platform. That's not what they
said they were selling of course, they said they were selling "easier Rails
deployment", but they were a platform.

-------

When I originally read the `"The Twelve-Factor App"`_, my thought was "Hmm,
these are some pretty ok ideas about how to build a website". I re-read it a
few months ago, and this time something clicked.

Twelve factor isn't a set of ideas about how to build web apps. It's a
description of a platform.

What's a platform? A platform is a contract between it, and the applications
that run on it. Viewed in this light, I began to understand much of twelve
factor more deeply. For example I originally thought the declaration that "The
twelve-factor app stores config in environment variables" was wrong, because I
didn't like environment variables. Now I understand that it means: "The
platform will make available any configuration values stored with it in the
application's POSIX environment".

This was a fundamentally different way of looking at it, and I didn't
recognize it at first, because almost no one deploying a web application has a
platform today, unless you use Heroku's or work someplace large like Twitter
or Google.

-------

This brings us back to DevOps. How does DevOps compare to a platform? DevOps
is all about ad-hoc. And the way I know this is that no two organizations on
the planet use the same Chef cookbook for deploying a Django application. Your
deployment is encoded in software, and that's good, but it's ad hoc and varies
from project to project. You can't write the "web app" side, without knowing
what the "Chef" side is as well.

DevOps was progress, now we have the same people writing the web app and the
Chef cookbook, which is way better than those being two unrelated groups which
hate each other.

A platform is about having a strict contract, an API if you will, which it
offers to applications, and which they then consume.

This model scales far better.

I think the *central element* of a platform is a scheduler. This lets you
address a group of computers instead of individual ones. Now you can express
actions like "run this container", where "this container" is something that
participates in the API of the platform. Now we can express "deploy a web
application" in terms of "schedule this container to run, if it ever stops
reschedule it, and expose these containers' locations to a reverse proxy".

A platform means APIs we can build on.

.. _`"The Twelve-Factor App"`: http://12factor.net/

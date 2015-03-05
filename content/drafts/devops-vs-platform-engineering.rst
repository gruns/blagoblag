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
Balancer as Platform as a Service is to ____________. If you answered
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

What's a platform? A platform is a suite of functionality that offers a
consistent contract to the applications that run on it. Viewed in this light,
I began to understand much of twelve factor more deeply. For example I
originally thought the declaration that "The twelve-factor app stores config
in environment variables" was wrong, because I didn't like environment
variables. Now I understand that it means: "The platform will make available
any configuration values stored with it in the application's POSIX
environment".

This was a fundamentally different way of looking at it, and I didn't
recognize it at first, because almost no one deploying a web application has a
platform built for that purpose today, unless you use Heroku's or work someplace
large like Twitter or Google. The platform most people are building on is
"Linux" and that's not designed to solve their problems.

-------

This brings us back to DevOps. How does DevOps compare to a platform? DevOps
is all about ad-hoc. And the way I know this is that no two organizations on
the planet use the same Chef cookbook for deploying a Django application. Your
deployment is encoded in software, and that's good, but it's ad hoc and varies
from project to project. You can't write the "web app" side, without knowing
what the "Chef" side is as well. Chef does not provide a consistent contract to
the application, what it provides is defined by the cookbook of the day -- the
only thing an application could assume is "Linux".

DevOps was progress, now we have the same people writing the web app and the
Chef cookbook, which is way better than those being two unrelated groups which
hate each other.

A platform is about having a strict contract, an API if you will, which it
offers to applications, and which they then consume.

Having a platform scales better than taking the "DevOps" approach, because a
platform means that deploying a new application does not require any new
coordination between teams or responsibilities. It also means a clear division
of responsibilities: the people who maintain the platform care about system
load, availability, and resiliency. The people deploying something on top of
it worry about bugs in their application or the performance of their
application.

Giving each side clear responsibilities makes applications easier to write,
and easier to deploy.


.. _`"The Twelve-Factor App"`: http://12factor.net/

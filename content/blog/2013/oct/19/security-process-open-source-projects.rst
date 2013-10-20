Security process for Open Source Projects
=========================================

:tags: community, django, open-source, python


This post is intended to describe how open source projects should handle
security vulnerabilities. This process is largely inspired by my involvement
in the `Django project`_, whose process is in turn largely drawn from the
`PostgreSQL project's`_ process. For every recommendation I make I'll try
to explain why I've made it, and how it serves to protect you and your users.
This is largely tailored at large, high impact, projects, but you should
able to apply it to any of your projects.

Why do you care?
----------------

Security vulnerabilities put your users, and often, in turn, their users at
risk. As an author and distributor of software, you have a responsibility to
your users to handle security releases in a way most likely to help them avoid
being exploited.

Finding out you have a vulnerability
------------------------------------

The first thing you need to do is make sure people can report security issues
to you in a responsible way. This starts with having a page in your
documentation (or on your website) which clearly describes an email address
people can report security issues to. It should also include a PGP key
fingerprint which reporters can use to encrypt their reports (this ensures
that if the email goes to the wrong recipient, that they will be unable to read
it).

You also need to describe what happens when someone emails that address. It
should look something like this:

#. You will respond promptly to any reports to that address, this means within
   48 hours. This response should confirm that you received the issue, and
   ideally whether you've been able to verify the issue or more information is
   needed.
#. Assuming you're able to reproduce the issue, now you need to figure out the
   fix. This is the part with a computer and programming.
#. You should keep in regular contact with the reporter to update them on the
   status of the issue if it's taking time to resolve for any reason.
#. Now you need to inform the reporter of your fix and the timeline (more on
   this later).

Timeline of events
------------------

From the moment you get the initial report, you're on the clock. Your goal is
to have a new release issued within 2-weeks of getting the report email.
Absolutely nothing that occurs until the final step is public. Here are the
things that need to happen:

#. Develop the fix and let the reporter know.
#. You need to obtain a CVE (Common Vulnerabilities and Exposures) number. This
   is a standardized number which identifies vulnerabilities in packages.
   There's a section below on how this works.
#. If you have downstream packagers (such as Linux distributions) you need to
   reach out to their security contact and let them know about the issue, all
   the major distros have contact processes for this. (Usually you want to give
   them a week of lead time).
#. If you have large, high visibility, users you probably want a process for
   pre-notifying them. I'm not going to go into this, but you can read about
   how Django handles this in `our documentation`_.
#. You issue a release, and publicize the heck out of it.

**Obtaining a CVE**

In short, follow `these instructions`_ from Red Hat.

What goes in the release announcement
-------------------------------------

Your release announcement needs to have several things:

#. A precise and complete description of the issue.
#. The CVE number
#. Actual releases using whatever channel is appropriate for your project (e.g.
   PyPI, RubyGems, CPAN, etc.)
#. Raw patches against all support releases (these are in addition to the
   release, some of your users will have modified the software, and they need
   to be able to apply the patches easily too).
#. Credit to the reporter who discovered the issue.

**Why complete disclosure?**

I've recommended that you completely disclose what the issue was. Why is that?
A lot of people's first instinct is to want to keep that information secret, to
give your users time to upgrade before the bad guys figure it out and start
exploiting it.

Unfortunately it doesn't work like that in the real world. In practice, not disclosing gives more power to attackers and hurts your users. Dedicated
attackers will look at your release and the diff and figure out what the
exploit is, but your average users won't be able to. Even embedding the fix
into a larger release with many other things doesn't mask this information.

In the case of yesterday's Node.JS release, which did not practice complete
disclosure, and did put the fix in a larger patch, this did not prevent
interested individuals from finding out the attack, it took me about five
minutes to do so, and any serious individual could have done it much faster.

The first step for users in responding to a security release in something they
use is to assess exposure and impact. Exposure means "Am I affected and how?",
impact means "What is the result of being affected?". Denying users a complete
description of the issue strips them of the ability to answer these questions.

What happens if there's a zero-day?
-----------------------------------

A zero-day is when an exploit is publicly available before a project has any
chance to reply to it. Sometimes this happens maliciously (e.g. a black-hat
starts using the exploit against your users) and sometimes it is accidentally
(e.g. a user reports a security issue to your mailing list, instead of the
security contact). Either way, when this happens, everything goes to hell in a
handbasket.

When a zero-day happens basically everything happens in 16x fast-forward. You
need to immediately begin preparing a patch and issuing a release. You should
be aiming to issue a release on the same day as the issue is made public.

Unfortunately there's no secret to managing zero-days. They're quite simply a
race between people who might exploit the issue, and you to issue a release and
inform your users.

Conclusion
----------

Your responsibility as a package author or maintainer is to protect your users.
The name of the game is keeping your users informed and able to judge their own
security, and making sure they have that information before the bad guys do.


.. _`Django project`: https://djangoproject.com
.. _`PostgreSQL project's`: http://www.postgresql.org/
.. _`our documentation`: https://docs.djangoproject.com/en/dev/internals/security/#who-receives-advance-notification
.. _`these instructions`: http://people.redhat.com/kseifrie/CVE-OpenSource-Request-HOWTO.html

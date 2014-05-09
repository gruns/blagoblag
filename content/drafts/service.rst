Service
=======

If you've been around an Open Source community for any length of time, you've
probably heard someone say, "We're all volunteers here". Often this is given as
an explanation for why some feature hasn't been implemented, why a release has
been delayed, or more generally, why something hasn't been done.

I think when we say these things (and I've said them as much as anyone), often
we're being dishonest. Almost always it's not a question of an absolute
availability of resources, but rather how we prioritize among the many tasks we
could complete. It can explain why we didn't have time to do things, but not
why we did them poorly.

Volunteerism does not place us above criticism, nor should it absolve us when
we err.

Beyond this however, many Open Source projects (including entirely volunteer
driven ones) don't just make their codebases available to others, they actively
solicit users, and make the claim that people can bet their businesses on this
software.

And yet, across a variety of policy areas, such as security and backwards
compatibility we often fail to properly consider the effects of our actions on
our users, particularly in a context of "they have bet their businesses on
this". Instead we continue to treat these projects as our hobbies projects, as
things we casually do on the side for fun.

Working on `cryptography`_, and security in general, has influenced my thinking
on these issues greatly. The nature of ``cryptography`` means when we make
mistakes, we put our users' businesses, and potentially their customers'
personal information at risk. This responsibility weighs heavily on me. It
means we try to have policies that emphasize review, it means we utilize
aggressive automated testing, it means we try to design APIs that prevent
inadvertent mistakes which affect security, it means we try to write excellent
documentation, and it means, should we have a security issue, we'll do
everything in our power to protect our users. (I've previous written about what
I think `Open Source projects' security policies should look like`_).

Open Source projects of a certain size, scope, and importance need to take
seriously the fact that we have an obligation to our users. Whether we are
volunteers, or paid, we have a solemn responsibility to consider the impact of
our decisions on our users. And too often in the past, we have failed, and
acted negligently and recklessly with their trust.

Often folks in the Open Source community (again, myself included!) have asked
why large corporations, who use our software, don't give back more. Why don't
they employ developers to work on these projects? Why don't they donate money?
Why don't they donate other resources (e.g. build servers)?

In truth, my salary is paid by every single user of Python and Django (though
`Rackspace`_ graciously foots the bill). The software I write for these
projects would be worth nothing if it weren't for the community around them, of
which a large part is the companies which use them. This community enables me
to have a job, to travel the world, and to meet so many people. So while
companies, such as Google, don't pay a dime of my salary, I gain a lot from
their usage of Python.

Without our users, we would be nothing, and it's time we started acknowledging
a simple truth: we exist in service of our users, and not the other way around.

.. _`cryptography`: https://cryptography.io/
.. _`Open Source projects' security policies should look like`: http://alexgaynor.net/2013/oct/19/security-process-open-source-projects/
.. _`Rackspace`: http://developer.rackspace.com/

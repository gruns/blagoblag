Telemetry for Open Source
=========================

What's the biggest difference between offering some functionality as an open
source library, and in offering it as an HTTP API? To me the single biggest
difference is that running a web service lets you instrument whats users are
using, and collect telemetry, while shipping an open source library doesn't.

For a combination of social and technical reasons, the open source community has
basically never added instrumentation to libraries which reports back to its
authors on how it's being used. The result is that open source maintainers have
considerably less information about what their users do with their product than
their peers writing web services.

I want to highlight just a few places where having the ability to collect usage
metrics would go a long way to improving the quality of open source:

Deprecations
------------

For a variety of reasons, from time to time, libraries deprecate functionality.
Unfortunately, right now open source maintainers have no data to inform how
disruptive a deprecation cycle is. Maintainers have only their own instinct, or
extreme non-representative surveys, to inform how many users are affected by a
deprecation.

In a world where open source libraries were highly instrumented, maintainers
could start by adding metrics on how often a feature they wanted to deprecate
was used. This would give a baseline on current usage. Maintainers could then
introduce deprecration warnings in the program and try to publicize the
deprecation. Finally, only when usage dropped below a threshold would the
deprecated functionality be removed.

This would provide a considerably better experience both for maintainers, who
could use actual data to make decisions, as well as for users who would be less
likely to inadvertently find themselves in the middle of a highly disruptive
breakage.

Other library version
---------------------

An extremely common question that faces open source maintainers is "What
versions of other *other* software are my users using?" This is everything from
what version of Python, what version of another Python library, or what version
of a system library? For `pyca/cryptography`_ we are constantly faced with the
issue of supporting a wide variety of OpenSSL versions.

Unfortunately we have no data on what versions most of our users are on. As a
result we hear exclusively from users who experience compatibility problems,
most of whom are using outrageously out of date versions of OpenSSL.

If we had actual data on what real users used, we could craft a much better
compatibility policy that ensured large swaths of our were supported, without
burdening the project by supporting tiny minorities.

Feature usage
-------------

Lots of open source projects claim to be targeting "80/20" use cases. Write 20%
of the code, serve 80% of the users. However, once again, there's basically
never any data to support their ideas about which features users actually need.

Armed with better data about which features are used, and which features aren't,
projects would have the opportunitty to craft better APIs, which address the
actual problems users have.

Conclusion
----------

Right now, open source maintainers have almost no data about how their libraries
are used with which to make decisions. The result is a lot of guess-work, and
deferring to a loud minority at the expense of the overwhelming majority.

If a culture emerged of users being ok with open source projects phoning home
with using statistics, and with open source projects using these to inform
decisions projects would be able to deliver better results.

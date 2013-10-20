
Thoughts on OpenStack
=====================

:tags: openstack, python, rackspace

Since I joined Rackspace a little over a month ago, I've gotten involved
with OpenStack, learning the APIs, getting involved in discussions, and
contributing code. I wanted to write a bit about what some of my experiences
have been, particularly with respect to the code and contribution process.

Architecture
------------

Were I to have started to design a system similar to OpenStack, and
particularly components like Swift (Object store), the first thing I would have
done would be build a (or select an existing) general purpose distributed
database. The OpenStack developers did not go in this direction, instead they
built tools specific to each of their needs. It's not yet clear to me whether
this is a better or worse direction, but it was one of the most striking things
to me.

Contribution
------------

Open Stack's contribution process is fantastic. Most open source projects have
a group of individuals who are committers (often called "core developers" or
similar) and the rest of the community contributes by sending patches, which
these committers merge. Eventually members of the community become
committers; this model is seen in projects like Django or CPython.

OpenStack flips this on its head. In OpenStack there are *no* committers. The
only thing that commits is a Jenkins instance. Instead, they have "core
reviewers". Essentially, to contribute to OpenStack, whether you're a long
standing member or brand new, you upload your patch with a ``git-review``
script to their Gerrit instance. People who follow that project in Gerrit are
notified, and Jenkins CI jobs are kicked off. People will review your patch,
and once it has both passing tests and the necessary number of "+1" reviews
from core reviewers, your patch is automatically merged.

This process of having no committers, only core reviewers, normalizes the
contribution process. Uploading a patch is the same experience for me, a
relative new comer, as it is for someone who's been working on the project from
the beginning. We just have slightly different review experiences. It also puts
an emphasis on code review, which I think is fantastic.

Code
----

OpenStack comprises a large amount of Python code, and I'm a very opinionated
Python developer. For the most part the OpenStack code is of good quality,
however there are a few issues I've run across:

* Most projects monkeypatch ``__builtin__``. Almost every OpenStack project
  monkeypatches this to add ``gettext`` as ``_``. This makes code remarkably
  difficult to read (you can never tell where it came from), and fragile. If
  you import files in the wrong order, suddenly you get a ``NameError``. I've
  been trying to work to remove these, and there seems to be some buy-in from
  the community on this.
* Most projects use a lot of global state around configuration. I've spoke
  about `why I dislike this approach before
  <https://www.youtube.com/watch?v=0FD510Oz2e4>`_. As with Django, I don't have
  a good suggestion as to how to fix it incrementally.

Infrastructure vs. Application Services
---------------------------------------

A lot of OpenStack's code is around what I like to think of as "infrastructure".
Things like spinning up VMs, storing disk images, taking snapshots, and
handling authentication for all of this. When OpenStack started there was one
application service, Swift, which does massively scalable object ("blob")
storage. One of the most exciting developments in OpenStack, in my opinion, is
the growth to include more application services, things that directly provide
utilities to your application. These include:

* Marconi: Queuing as a service, I'm working on a ``kombu`` backend so that if
  you're deployed in an OpenStack cloud with Marconi, having a job queue system
  will be a matter of a few seconds work with ``celery``.
* Trove: Relational databases as a service, spin up database instances, back
  them up, restore, and monitor.
* Designate: DNS as a service.
* Libra: Load balancer as a service.
* Barbican: Secrets as a service, this will be able to manage things like your
  ``SECRET_KEY`` in Django, to avoid forcing you to put it on disk or in your
  project's source.

It's worth noting that many of these are still "StackForge" projects, which
means it's not guarnteed that they'll become a part of OpenStack, nevertheless
I think these are exciting developments.

Of particular value is that, because they're (of course) open source, you're
spared some of the lock-in concerns that come from many "as a service"
offerings.

Future involvement
------------------

Looking towards the future, I'm hoping to be involved with OpenStack primarily
in three ways:

* Making it run, idiotically fast, on PyPy. Right now this means I'm working on
  making ``sqlalchemy``, which many Open Stack projects use, fast on PyPy.
* Working on ``opentls``, which is a pure python binding to OpenSSL. This also
  furthers the first goal of getting OpenStack running on PyPy, as well as
  hopefully contributing to the overall system security.
* Getting a ``kombu`` backend for Marconi, so Open Stack users can have
  basically drop-in queuing with ``celery``.

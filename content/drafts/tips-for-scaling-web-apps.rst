Tips for Scaling Web Apps
=========================

This blog post is a short list of things you can do, on basically any web
project, to improve performance, scalability, and cost. In 2015, a medium
sized server (8 cores, 24GB of RAM) is capable of serving
hundreds-to-thousands of HTTP requests per second. This post is a guide to
making sure you aren't wasting your resources on things that are already
solved problems.

All of these assume you have monitoring to track your availability, and
metrics to track various aspects of your site's performance. You want to be
looking at 99th percentile numbers, not 50th percentile. A 50th percentile
page load time means **half** of your users are experiencing something slower,
so this can be very misleading.

Many of these are things you can do right from the start, not lessons you need
to learn the hard way.

Static Assets
-------------

Put all your static assets (CSS, Javascript, Images) behind a CDN that reverse
proxies to your servers and caches stuff at their PoPs. This will get you good
performance for users and effectively infinite scalability (for static assets).

Assets should all have unique names for content. That means when you change
the contents of a Javascript file your asset pipeline should give the final
file your webservers serve a unique name. This lets you set HTTP caching
headers for the far future, which lets web browsers actually cache the data on
users' computers, saving you entire HTTP requests. A simple trick to get a
unique name is to make the filename that your asset pipeline emits simply be
the ``sha256`` of the file's contents.

Sessions
--------

If you can get away with it, storing your session as a signed (and optionally
encrypted) cookie is great, this saves you from needing to do any database
lookups on your server. You should be using TLS for all connections, and
setting the secure flag on the cookie. And for the love of god, do not
implement the crypto signing/encrypting/verifying/decrypting bits yourself.
Use an `existing library`_.

If signed cookies are insufficient for some reason (e.g. large payload size),
your best bet is to use a simple K/V store. For most applications, best-effort
persistence is sufficient, so something dirt simple like memcached works
great.

Load balancing
--------------

Your web nodes should be stateless. Put them behind a load balancer from the
beginning, and practice (read: develop automation for) adding and removing
them. It should be completely trivial and safe for you to add web nodes whenever
you need to, and delete old nodes for any reason.

If your load balancer lets you pick a distribution strategy, minimum number of
connections is a safe bet.

Set up your load balancer to perform health checks on the backends every
couple of seconds.

Object storage
--------------

For things like user uploads, or other blob storage (any static media that
isn't a part of the site itself), use an object storage API (Amazon's S3 is
the gold standard). Avoid local disk: it's hard to scale and not worth the
effort, hosted solutions are cheap and easy.

Databases
---------

For most applications, a simple relational database is fine. Further, most
applications become bottlenecked on reads well before they become bottlenecked
on writes.

It should be easy for you to set up additional read replicas as needed, and to
get application servers performing queries against them. Monitor the
replication lag from the primary to the replicas.

Develop automation for failing over your primary to a secondary.

For any analytics workloads you have (reports, dashboards, or unusual
administrative pages) have an additional read replica that is specific to
them. Analytics workloads tend to "look" different from regular transactional
queries, and mixing them on a single server can degrade performance due to
excessive trashing of caches.

Don't rely on database migrations being fast. Your application code should be
able to handle the database in the "pre-migration", "post-migration", and
"during-migration" states. For example, to add a new column you'd have the
following steps:

#. Add a new nullable column to your database.
#. Deploy application code to write to that column.
#. Run a script in the background to backfill the data for older rows.
#. Verify the integrity of all the data.
#. Finally, deploy application code to actually read from the column.

Deployment and Automation
-------------------------

Any maintenance task you perform should be encoded in software.

Actually *practice* your automation. Delete and replace servers all the time,
this is the only way to make it easy and safe.

Practical load testing can be extremely difficult. Leverage "dark reads" to
practically measure the capacity of your site. Dark reads are where you have
visitors to your site make requests to an endpoint in the background (e.g.
with an AJAX request), but don't actually do anything with the responses. This
lets you measure the performance of a new feature based on more realistic load
patterns.

In a similar vein, rather than meticulous branch maintenance and testing
environments, use feature flags to deploy new changes instantly, but only make
them available to certain subsets of users.

Your team
---------

It's quite likely that scaling up your team will be the hardest thing you do.
Write tests and documentation, and use linters and code review to ensure the
quality of your code and knowledge sharing amongst team members.

.. _`existing library`: https://pythonhosted.org/itsdangerous/

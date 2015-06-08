Tips for Improving Your Company's Security
==========================================

Security is hard. That's not a secret. Defenders need to be perfect, attackers
only need to find one mistake.

That said, there's a lot you can do to improve your company's security.

User Credentials
----------------

Store your users' passwords for your site responsibly. This means using PBKDF2
(with high iteration count), bcrypt, or scrypt. There's no reason for you to use
anything else.

Offer two factor authentication for your users. If your product is for teams,
make it easy for administrators to check if their team members have two factor
enabled, and require it.

**Do not** require your users to rotate their passwords. This practice just
encourages them to use weaker passwords.

SSH
---

Require two factor authentication for *all* SSH access to your servers. Products
such as `Duo`_ make this straightforward.

Avoid people needing to SSH into things at all: for example, have a centralized
logging system which aggregates logs from multiple systems.

Network
-------

Do not trust your network. When two servers need to communicate with each other,
use an authenticated and encrypted channel (e.g. TLS).

Patching
--------

Aggressively stay up to date on applying patches, even if the bugs they fix
don't seem relevant.

Remember, complex systems failures do not occur because one thing is broken in a
really subtle way, they occur because multiple components had independent
failures which combined, like a toxic drug interaction.

Maintain your systems in such a way that it's easy for you to patch things and
do rolling restarts. Applying a patch **must** not be a disruptive activity.

Education
---------

Developers should be familiar with basic security vulnerabilities for whatever
space you're working in. For example, developers working on web applications
should be familiar with SQL injection and cross-site scripting.

.. _`Duo`: https://www.duosecurity.com/product/applications/unix-ssh

Your Distro's Definition of a Security Issue is Wrong
=====================================================

Linux distributions are interesting pieces of software. Unlike traditional
commercial operating systems (Windows or OS X), they don't build the kernel or
the userspace applications [#]_. Instead, most of what actually gets built as a
part of a Linux distribution is tooling to bring everything together. Most
notably, this includes a package manager and a (usually curated) set of
packages that can be installed.

The repository of packages is central to a Linux distribution's value
proposition. Basically every distro makes a promise like: If you install
packages from our repository, we'll take responsibility to making sure that all
the security patches are applied and that things work nicely with each other.

Security packages as a service! It's a great promise; the burden on individual
developers and sysadmins to keep track of vulnerabilities in the myriad of
software packages they use would be enormous, no one would ever manage to ship
any software (or secure it)!

The distro's appear to use a definition of security issues that is:

    A specific bug in a specific piece of software that results in a specific
    vulnerability (that someone, under some threat model, could exploit)

This is not unreasonable. Unfortunately, it's also not sufficient. In the era
of nearly ubiquotsly networked computing, there is a second set of security
issues: emergent ones which do not occur because any piece of software has a
vulnerability, but rather because a set of incentives and *features* have
resulted in a less secure ecosystem.

That's a bit abstract, let's look at some specific examples.

1024-bit root certificates
--------------------------

* Old OpenSSL's which don't handle chain certs preventing the removal of 1024-bit roots


SHA-256 certificates
--------------------

* Old NSS which don't handle something about the SHA256 migration preventing the removal of SHA1 certs

pip RCE
-------

* Debian's pip has a trivial RCE

Conclusion
----------


* Distros need to be more aggressive in upgrading to the latest versions of software
* Packages need to be better about packages compatibility so that distros can ship newer versions. It's not like "every 6-18 months everything breaks" was acceptable anyways.


.. [#] Though many companies which produce Linux distributions *also* pay people to work on the kernel and various components of one of the Linux userspace stacks.

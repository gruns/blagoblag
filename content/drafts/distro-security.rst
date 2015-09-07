Your Distro's Definition of a Security Issue is Wrong
=====================================================

Outline:

* Distro's (particularly LTS) value proposition is that they will make sure their packages get patched for security issues
* Describe the definition of security issues they use
* This definition is overly limiting, resulting in *emergent* security issues which do not have a natural locus the way their process would like
* Examples:

    * Old OpenSSL's which don't handle chain certs preventing the removal of 1024-bit roots
    * Old NSS which don't handle something about the SHA256 migration preventing the removal of SHA1 certs

* Also sometimes distros are lazy

    * Debian's pip has a trivial RCE

* Conclusion

    * Distros need to be more aggressive in upgrading to the latest versions of software


Thoughts on Lavabit
===================


If you haven't already, you should start by reading `Wired's article on this`_.

I am not a lawyer. That said, I want to walk through my take on each stage of
this.

The government served Lavabit with an order requiring them to supply metadata
about every email, as well as mailbox accesses, for a specific user. Because
this was "metadata" only the government was not required to supply probable
cause.

First, it should be noted that metadata isn't a thing. There's not a
definition, it has no meaning. There's simply data.

Lavabit refused to comply, whereupon the government filed a motion requiring
them to comply, which a US magistrate so ordered.

And here's where things go wrong. The magistrate erred in ordering compliance.
While an argument could be made (note: I'm not making this argument) that in
general, certain metadata does not have an expectation of privacy, Lavabit
operates a specialized service. Immediately upon receipt of mail, it's
encrypted with a user's public key. After that it's technically impossible for
the service to read the plaintext of a user's email. This relationship creates
a strong expectation of privacy, and the Fourth Amendment very explicitly
requires a warrant supported by probably cause at this point.

But let's ignore this first order. Lavabit has, in past, complied with lawful
search warrants, and there's no reason to believe they would not have been able
to comply with a lawfully constructed one here.

Following this the FBI obtained a warrant requiring that Lavabit turn over
their SSL private key. The application for, and issue of, this warrant
unambiguously violated Lavabit's constitutional protection. The Fourth
Amendment requires that a warrant describe specifically where is to be
searched, and what they're looking for.

Access to Lavabit's private key would allow someone with the raw internet
traffic (which presumably the FBI, had access to) to decrypt and read *any*
user's emails before they reached Lavabit's servers. Simply put, this was a
warrant issued in flagrant violation of the United State Constitution.

The fact that Lavabit refused to cooperate with the government's original order
in no way gave them the right to apply (or be granted) the follow up order.
Failure to comply with a lawfully issued warrant can result in fines, or even
jail time, but it does not grant the government extra-legal authority.

The entirety of this case, but particularly the government's second request,
demonstrate a travesty of immense proportions. The assumptions I grew up with
about my legal protections as an American are rapidly being shown to be
illusory. Lavabit's founder is `raising money to support his legal defense`_,
I've donated and I hope you will too.

.. _`Wired's article on this`: http://www.wired.com/threatlevel/2013/10/lavabit_unsealed/
.. _`raising money to support his legal defense`: https://rally.org/lavabit

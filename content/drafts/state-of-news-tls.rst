The State of the News and TLS
=============================

I've `previously written about the importance of TLS`_. There are few domains
that I can imagine the protections TLS offers are more important for than the
news. The idea that articles I read could be manipulated be an attacker on the
network is absolutely frightening to me, and the fact that I have no privacy
from anyone else on the network with respect to which articles I'm reading is
similarly disturbing.

Given the *obvious* importance of privacy, authentication, and integrity for
critical news, I wanted to see how the top news papers did, in terms of
offering, and hopefully even requiring TLS, for their websites. Here's how the
top ten newspapers, by circulation in the US, did:

* The Wall Street Journal: **No TLS**
* The New York Times: **No TLS**
* USA Today: **No TLS**
* Los Angeles Times: **No TLS**
* Daily News: **TLS technically available, but badly mis-renders due to blocked content**
* New York Post: **No TLS**
* The Washington Post: **No TLS**
* Chicago Sun-Times: **TLS available, but not required**
* The Denver Post: **No TLS**
* Chicago Tribune: **No TLS**

Not so hot. Of the top 10, only one has a functioning TLS deployment, and it
doesn't require TLS. Almost all of the rest redirect HTTPS back to HTTP, or
fail with a certificate error (many of them for Akamai).

Ok, maybe print newspapers aren't the best place to look. So I combed through
the Alexa Top 150, looking for news websites to see how they did, these are
companies with major internet presences, surely they'll do better (I've
excluded sites that were also present in the first list):

* ESPN: **TLS technically available, but badly mis-renders due to blocked content**
* CNN: **No TLS**
* Fox News: **No TLS**
* Forbes: **No TLS**
* The Daily Mail UK: **No TLS**
* CBS Sports: **TLS technically available, but badly mis-renders due to blocked content**
* BBC: **No TLS**
* NPR: **No TLS**
* TMZ: **TLS available, HTTP redirects to HTTPS**
* NBC News: **No TLS**
* ABC News: **TLS technically available, but badly mis-renders due to blocked content**
* Time: **TLS technically available, but page doesn't fully function due to blocked content**

There you have. The news website with the best TLS on the internet is TMZ.

We should be embarrassed by this pathetic state of TLS deployment for critical
news outlets.

If you, the reader, work for one of these websites, please, advocate internally
for prioritizing the availability of TLS, and redirecting HTTP traffic to
HTTPS.

Everyone else, please reach out to the news websites you read to ask them for
TLS, to predict you, the reader's, privacy and the integrity and authenticity
of your access to these websites.

Surely a fundamental component of a free press, ultimately necessary for a
functioning democracy, is the ability of the people to access the press
uninterrupted.

.. _`previously written about the importance of TLS`: https://alexgaynor.net/2014/oct/06/http-considered-unethical/

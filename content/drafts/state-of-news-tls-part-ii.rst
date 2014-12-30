The State of the News and TLS: Part II
======================================

About six weeks ago I blogged about the `state of the news and TLS`_. Spoiler
alert, it wasn't great. Happily, there's been some good news on this front.

First, the New York Times wrote `a piece calling for more news websites to
expose their content over TLS`_. While the Times is not yet available over
TLS, based on this post I'm hopeful it will happen in 2015.

The second major piece of news was the Chrome Security Team's `announcement of
their plans`_ to move towards a negative security-indicator for plain-HTTP
websites. Better informing users as to what the security implications are when
websites don't respect user's privacy and readership will hopefully be a major
step forward in pushing website operators to offer and require TLS.

Given these pieces of news, let's see how major newspapers are doing:

* The Wall Street Journal: **No TLS**
* The New York Times: **No TLS**
* USA Today: **No TLS**
* Los Angeles Times: **No TLS**
* Daily News: **TLS technically available, but badly mis-renders due to blocked mixed content**
* New York Post: **No TLS**
* The Washington Post: **No TLS**
* Chicago Sun-Times: **No TLS**
* The Denver Post: **No TLS**
* Chicago Tribune: **No TLS**

Net change over last month? The Chicago Sun-Times actually *regressed*. Last
month they had a working deployment, now it's a certificate error.

Let's see how other major news sites are doing:

* ESPN: **TLS technically available, but badly mis-renders due to blocked mixed content**
* CNN: **No TLS**
* Fox News: **No TLS**
* Forbes: **No TLS**
* The Daily Mail UK: **No TLS**
* CBS Sports: **TLS technically available, but badly mis-renders due to blocked mixed content**
* BBC: **No TLS**
* NPR: **No TLS**
* TMZ: **TLS available, but not required**
* NBC News: **No TLS**
* ABC News: **TLS technically available, but badly mis-renders due to blocked mixed content**
* Time: **No TLS**

The change here was a regression for Time, which used to have semi-functional
TLS, and now they redirect HTTPS requests over to HTTP.

All in all, despite the good news from the New York Times and Chrome's Security
Team, on a technical level, it's been a crummy month for TLS.

There are two things I'd like to draw attention to:

First, many of these websites *technically* have TLS, they listen on port 443,
and even have an HTTP server running, but all they do is redirect to HTTP on
port 80. This is unfortunate. However, it makes clear that the issue is not
obtaining certificates or anything like that.

What I have heard identified as a major issue many many times is advertising
providers either not offering TLS or having reduced inventory with HTTPS. This
incentivizes websites to redirect over to HTTP, lest they lose revenue.

I'm not unsympathetic to the difficulties this can cause for a news website
interested in TLS. However, I don't think it excuses the silence from these
sites on HTTPS. If you are a news site who would like to offer HTTPS, but is
unable to because of your advertisers: **talk about it**. You are a newspaper,
and this is a story in the public interest.

In the meantime, I'm hopeful that Chrome's proposed changes will help swing the
pendulum towards incentivizing TLS.


.. _`state of the news and TLS`: https://alexgaynor.net/2014/nov/12/state-of-news-tls/
.. _`a piece calling for more news websites to expose their content over TLS`: http://open.blogs.nytimes.com/2014/11/13/embracing-https/
.. _`announcement of their plans`: http://www.chromium.org/Home/chromium-security/marking-http-as-non-secure

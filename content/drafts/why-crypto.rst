Why Crypto
==========

People who follow me on twitter or github have probably noticed over the past
six months or so: I've been talking about, and working on, cryptography a lot.
Before this I had basically zero crypto experience. Not a lot of programmers
know about cryptography, and many of us (myself included) are frankly a bit
scared of it. So how did this happen?

At first it was simple: PyCrypto (probably the most used cryptographic library
for Python) didn't work on PyPy, and I needed to perform some simple
cryptographic operations on PyPy. Someone else had already started work on a
``cffi`` based cryptography library, so I started trying to help out.
Unfortunately the maintainer had to stop working on it. At about the same time
several other people (some with much more cryptography experience than I)
expressed interest in the idea of a new cryptography library for Python, so we
got started on it.

Since then I've been in something of a frenzy, reading and learning everything
I can about cryptography. And while originally my motivation was "a thing that
works on PyPy", I've now grown considerably more bold:

Programmers are used to being able to pick of domain knowledge as we go. When I
worked on a golf website, I learned about how people organized golf outings,
when I worked at rdio I learned about music licensing, etc. Programmers will
apply their trade to many different domains, so we're used to learning about
these different domains with a combination of Google, asking folks for help,
and looking at the result of our code and seeing if it looks right.

Unfortunately, this methodology leads us astray: Google for many cryptographic
problems leaves you with a pile of wrong answers, very few of us have friends
who are cryptography experts to ask for help, and one can't just look at the
result of a cryptographic operation and see if it's security. Security is a
property much more subtle than we usually have to deal with:

.. code-block:: pycon

    >>> encrypt(b"a secret message")
    b'n frperg zrffntr'

Is the ``encrypt`` operation secure? Who knows!

Correctness in this case is dictated by analyzing the algorithms at play, not
by looking at the result. And most of us aren't trained by this. In fact we've
been *actively encouraged* not to know how. Programmers are regularly told
"don't do your own crypto" and "if you want to do any crypto, talk to a real
cryptographer". This culture of ignorance about cryptography hasn't resulted in
us all contacting cryptographers, it's resulted in us doing bad crypto:

.. raw:: html

    <blockquote class="twitter-tweet" lang="en"><p>20 years of abstinence-only cryptography education hasn’t gotten us anything but an endless supply of bad crypto in production systems.</p>&mdash; David Reid (@dreid) <a href="https://twitter.com/dreid/statuses/422799924225273856">January 13, 2014</a></blockquote>
    <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Usually when we design APIs, our goal is to make it easy to do *something*.
Crypotographic APIs seem to have been designed on the same principle.
Unfortunately that something is almost never secure, in fact, in many
libraries, the path of least resistance leads you to doing something that is
extremely wrong.

So we set out to design a better library, with the following principles:

* It should never be easier to do the wrong thing than it is to do the right
  thing.
* You shouldn't need to be a cryptography expert to use it, our documentation
  should equip you to make the right decisions.
* Put our users' safety and security above all else.

I'm very proud of our work so far. You can find `our documentation online`_.
We're not done. We have many more types of cryptographic operations left to
expose, and more recipes left to expose. But the work we've done so far has
stayed true to our principles. Please let us know if our documentation ever
fails to make something accessible to you.

.. _`our documentation online`: https://cryptography.io

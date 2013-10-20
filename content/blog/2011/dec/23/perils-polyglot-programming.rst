
The perils of polyglot programming
==================================

:tags: djangocon, programming, programming-languages

Polyglot programming (the practice of knowing and using many programming
languages) seems to be all the rage these days. Its adherents claim two
benefits:

1. Using the right tool for every job means everything you do is a little
   bit easier (or better, or faster, or all of the above).
2. Knowing multiple programming paradigm expands your mind and makes you
   better at programming in every language.


I'm not going to dispute either of these. Well, maybe the second I'll argue
with a little: I think you can get most of the benefits by using different
paradigms within the same multi-paradigm language, and I'm a bit skeptical
of the global benefits (unless you're the type of person who likes writing
FORTRAN in Javascript). But I digress, like I said, I think those are both
fair claims.

What I don't like is the conclusion that this means you should always use the
right tool for the job. What, you the astute reader asks, does this mean you
think we should use the *wrong* tool for the job? No, that would be idiotic,
it means I think sometimes using the less optimal tool for the job carries
overall benefits.

So what are the dangers of being a polyglot programmers (or the benefits of 
not being one, if you will)?

Using multiple languages (or any technology) stresses your operations people.
It's another piece they have to maintain. If you've got a nice JVM stack, top
to bottom, with nice logging and monitoring do you think your ops people
really want to hear that they need to duplicate that setup so you can run
three Ruby cron jobs? No, they're going to tell you to suck it up and write it
up and either see if JRuby works or use Clojure or something, because 1% of
your company's code isn't worth doubling their work.

Another risk is that it raises the requirements for all the other developers
on the project. Martin Golding said, "Always code as if the guy who ends up
maintaining your code will be a violent psychopath who knows where you live."
Imagine when you leave your job and the next guy finds out you decided to
write some data analysis scripts in APL (for those of you who don't remember,
APL is that lovely language that doesn't use ASCII characters). It's fine to
use APL if that's something you can require of new hires, it's not fine when
your job says "Python developer" (it may actually work for Perl developers,
but I assure you it'll be purely coincidental). Learning a new language is
hard, learning to write it effectively is harder. Learning a new language for
every script you have to maintain is downright painful, and once you know all
of them, context switching isn't free for either humans or computers.

I'm not saying write everything in one language, that'd probably leave you
writing a lot of code in very suboptimal languages. But choose two or three,
not ten. Your ops people will thank you, and so will the guys who have to
maintain your code in a decade. At DjangoCon this year Glyph Lefkowitz
actually went farther, he argued that not just the code you write, but your
entire technology stack should be in one language. But that's a separate
discussion, you should watch `the video`_ though.

Also, because I'm a big fan of The West Wing, I'd be remiss if I used the word
polyglot this many times without `linking to a great scene`_.

.. _`the video`: https://blip.tv/djangocon/keynote-glyph-lefkowitz-5573264
.. _`linking to a great scene`: https://www.youtube.com/watch?v=TIq7S71AYcQ

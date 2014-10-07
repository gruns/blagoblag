How to Code Review Without Being a Jerk
=======================================

Last year I wrote about how `it was possible to do code review without being a
jerk`_, but I didn't show you how. Linus and LKML, once again, find themselves in
the spotlight, so I thought I would show how it can be done.

On a whim today, I clicked on a `random message from Linus`_, here's what I
found::

    Yeah, this is pure crap. It doesn't even compile.

        drivers/media/dvb-frontends/si2165.c:1063:17: error: expected ‘,’ or ‘;’ before ‘SI2165_FIRMWARE’
        MODULE_FIRMWARE(SI2165_FIRMWARE);

    because it should presumably say "SI2165_FIRMWARE_REV_D" now.

    Why the f*ck do you send me totally untested crap?

                     Linus


Here's how I would have given that code review::


    Right now the code doesn't compile with your patch applied. Here's the
    error message I'm getting:

        drivers/media/dvb-frontends/si2165.c:1063:17: error: expected ‘,’ or ‘;’ before ‘SI2165_FIRMWARE’
        MODULE_FIRMWARE(SI2165_FIRMWARE);

    I think that should probably be "SI2165_FIRMWARE_REV_D" instead.

    Please be sure to test your patches before submitting them in the future.

    Thanks for contributing! :sparkles:
    Alex

That's seriously all it takes to let your contributors know their work is
appreciated, and to not be a jerk.

.. _`it was possible to do code review without being a jerk`: https://alexgaynor.net/2013/jul/16/you-dont-have-be-jerk-code-review/
.. _`random message from Linus`: https://lkml.org/lkml/2014/10/3/407

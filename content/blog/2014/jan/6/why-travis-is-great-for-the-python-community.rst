Why Travis CI is great for the Python community
===============================================

In the unlikely event you're both reading my blog, and have not heard of Travis
CI, it's a CI service which specifically targets open source projects. It
integrates nicely with Github, and is generally a pleasure to work with.

I think it's particularly valuable for the Python community, because it makes
it easy to test against a variety of Pythons, which maybe you don't have at
your fingertips on your own machine, such as Python 3 or PyPy (Editor's note:
Why aren't you using PyPy for all the things?).

Travis makes this drop dead simple, in your ``.travis.yml`` simply write:

.. code-block:: yaml

    language: python
    python:
        - "2.6"
        - "2.7"
        - "3.2"
        - "3.3"
        - "pypy"

And you'll be whisked away into a land of magical cross-Python testing. Or, if
like me you're a fan of ``tox``, you can easily run with that:

.. code-block:: yaml

    python: 2.7
    env:
        - TOX_ENV=py26
        - TOX_ENV=py27
        - TOX_ENV=py32
        - TOX_ENV=py33
        - TOX_ENV=pypy
        - TOX_ENV=docs
        - TOX_ENV=pep8

    script:
        - tox -e $TOX_ENV

This approach makes it easy to include things like linting or checking your
docs as well.

Travis is also pretty great because it offers you a workflow. I'm a big fan of
code review, and the combination of Travis and Github's pull requests are
awesome. For basically every project I work on now, I work in this fashion:

* Create a branch, write some code, push.
* Send a pull request.
* Iteratively code review
* Check for travis results
* Merge

And it's fantastic.

Lastly, and perhaps most importantly, Travis CI consistently gets better,
without me doing *anything*.

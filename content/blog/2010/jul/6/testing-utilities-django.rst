
Testing Utilities in Django
===========================

:tags: django, fixtures, python, testing, tests

Lately I've had the opportunity to do some `test-driven development <http://en.wikipedia.org/wiki/Test-driven_development>`_ with Django, which a) is awesome, I love testing, and b) means I've been working up a box full of testing utilities, and I figured I'd share them.

Convenient ``get()`` and ``post()`` methods
-------------------------------------------

If you've done testing of views with Django you probably have some tests that look like:

.. sourcecode:: python
    
    def test_my_view(self):
        response = self.client.get(reverse("my_url", kwargs={"pk": 1}))
        
        response = self.client.post(reverse("my_url", kwargs={"pk": 1}), {
            "key": "value",
        })

This was a tad too verbose for my tastes so I wrote:

.. sourcecode:: python

    def get(self, url_name, *args, **kwargs):
        return self.client.get(reverse(url_name, args=args, kwargs=kwargs))
    
    def post(self, url_name, *args, **kwargs):
        data = kwargs.pop("data", None)
        return self.client.post(reverse(url_name, args=args, kwargs=kwargs), data)

Which are used:

.. sourcecode:: python
    
    def test_my_view(self):
        response = self.get("my_url", pk=1)
        
        response = self.post("my_url", pk=1, data={
            "key": "value",
        })

Much nicer.

``login()`` wrapper
-------------------

The next big issue I had was logging in and out of multiple users was too verbose.  I often want to switch between users, either to check different permissions or to test some inter-user workflow.  That was solved with a simple context manager:

.. sourcecode:: python
    
    class login(object):
        def __init__(self, testcase, user, password):
            self.testcase = testcase
            success = testcase.client.login(username=user, password=password)
            self.testcase.assertTrue(
                success,
                "login with username=%r, password=%r failed" % (user, password)
            )
        
        def __enter__(self):
            pass
        
        def __exit__(self, *args):
            self.testcase.client.logout()
    
    def login(self, user, password):
        return login(self, user, password)

This is used:

.. sourcecode:: python
    
    def test_my_view(self):
        with self.login("username", "password"):
            response = self.get("my_url", pk=1)

Again, a lot better.

django-fixture-generator
------------------------

Not quite a testing utility, but my app `django-fixture-generator <http://github.com/alex/django-fixture-generator>`_ has made testing a lot easier for me.  Fixtures are useful in getting data to work wit, but maintaining them is often a pain, you've got random scripts to generate them, or you just checkin some JSON to your repository with no way to regenerate it sanely (say if you add a new field to your model).  django-fixture-generator gives you a clean way to manage the code for generating fixtures.


In general I've found context managers are a pretty awesome tool for writing clean, readable, succinct tests.  I'm sure I'll have more utilities as I write more tests, hopefully someone finds these useful.

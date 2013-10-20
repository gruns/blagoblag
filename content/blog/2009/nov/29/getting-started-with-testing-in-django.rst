
Getting Started with Testing in Django
======================================

:tags: django, python, tests

Following yesterday's post another hotly requested topic was testing in Django.  Today I wanted to give a simple overview on how to get started writing tests for your Django applications.  Since Django 1.1, Django has automatically provided a tests.py file when you create a new application, that's where we'll start.

For me the first thing I want to test with my applications is, "Do the views work?".  This makes sense, the views are what the user sees, they need to at least be in a working state (200 OK response) before anything else can happen (business logic).  So the most basic thing you can do to start testing is something like this:

.. sourcecode:: python
    
        from django.tests import TestCase
        class MyTests(TestCase):
            def test_views(self):
                response = self.client.get("/my/url/")
                self.assertEqual(response.status_code, 200)

By just making sure you run this code before you commit something you've already eliminated a bunch of errors, syntax errors in your URLs or views, typos, forgotten imports, etc.  The next thing I like to test is making sure that all the branches of my code are covered, the most common place my views have branches is in views that handle forms, one branch for GET and one for POST.  So I'll write a test like this:

.. sourcecode:: python
    
        from django.tests import TestCase
        class MyTests(TestCase):
            def test_forms(self):
                response = self.client.get("/my/form/")
                self.assertEqual(response.status_code, 200)
    
                response = self.client.post("/my/form/", {"data": "value"})
                self.assertEqual(response.status_code, 302) # Redirect on form success
    
                response = self.client.post("/my/form/", {})
                self.assertEqual(response.status_code, 200) # we get our page back with an error

Now I've tested both the GET and POST conditions on this view, as well the form is valid and form is invalid cases.  With this strategy you can have a good base set of tests for any application with not a lot of work.  The next step is setting up tests for your business logic.  These are a little more complicated, you need to make sure models are created and edited in the right cases, emails are sent in the right places, etc.  `Django's testing documentation <http://docs.djangoproject.com/en/dev/topics/testing/>`_ is a great place to read more on writing tests for your applications.

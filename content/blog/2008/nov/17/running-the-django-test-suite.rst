
Running the Django Test Suite
=============================

:tags: django, tests

This question came up in IRC yesterday, so I figured I'd run through it today.  Django has a very extensive test suite that tests all of the components of Django itself.  If you've ever written a patch for Django you probably know that tests are a requirement, for both new features and bug fixes.  I'm going to try to run down how to setup your own testing envrioment.

First you need to have Django installed somewhere, for now I'll assume you have it in ~/django_src/.  Somewhere on your python path, go ahead are use django-admin.py to create a new project.  I've named this project django_test.  Next, inside of that project create a folder named settings, and move settings.py into that folder and renmae it __init__.py.  The reason we're going to have a settings directory is so that we can have subsettings for individual scenarios.  Put some default settings for the various field in there now, for example my default settings provides the necessary options for SQLite.  Now if there are any other subsettings you wish to setup create a file for them in the settings directory, and at the top of this file put from django_test.settings import \*, followed by whatever settings you wish to overide.  For example I have a mysql.py that overides my default SQLite database settings with MySQL values.

Now that we have our test settings, go to the directory where you have Django installed.  To run the tests do ./tests/runtests.py --settings=django_test.settings.  You can also use the DJANGO_SETTINGS_MODULE enviromental variable in place of passing in the settings like this.  You can also provide a verbosity argument, the default is 0, I prefer to run with verbosity=1 because this keeps you up to date on the progress of the tests, without too much extraneus output.

Usually when you are working on a patch you don't need to run the entire test suite, your patch only affects a few tests.  Therefore, you can provide a list of tests you'd like to run, so for example you could do ./tests/runtests.py --settings=django_test.settings.mysql -v 1 model_forms model_formsets.  This will run the model_forms and model_formsets tests, with your mysql settings, at verbosity level 1.

And that's all it takes to run the Django test suite.

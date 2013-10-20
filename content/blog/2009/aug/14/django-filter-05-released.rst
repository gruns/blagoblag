
Django-filter 0.5 released!
===========================


I've just tagged and uploaded Django-filter 0.5 to PyPi.  The biggest change this release brings is that the package name has been changed from `filter` to `django_filters` in order to avoid conflicts with the Python builtin `filter`.  Other changes included the addition of an `initial` argument on Filters, as well as the addition of an `AllValuesFilter` which is a `ChoiceFilter` who's choices are any values currently in the DB for that field.  Despite the change in package name I will not be changing the name of the project due to the overhead in moving the repository (Github doesn't set up redirects when you change a project's name) and the PyPi package.  I hope everyone enjoys this new release, as a lot of it's improvements have come out of my usage on Django-filter in piano-man.

As for what the future holds several people have indicated their interest in the inclusion of django-filter in Django itself as a contrib package, and for usage in the Admin as a new implementation of the `list_filter` option that is more flexible.  Because of this my next work is probably going to be on implementing a custom `ModelAdmin` class that uses `FilterSets` for filtering.

You can find the latest release on `PyPi <http://pypi.python.org/pypi/django-filter>`_ and `Github <http://github.com/alex/django-filter/tree/master>`_.

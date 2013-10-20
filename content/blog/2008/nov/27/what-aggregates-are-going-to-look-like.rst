
What aggregates are going to look like
======================================


Prior to Django 1.0 there was a lot of discussion of what the syntax for doing aggregate queries would like.  Eventually a syntax was more or less agreed upon, and over the summer Nicolas Lara implemented this for the Google Summer of Code project, mentored by Russell Keith-Magee.  This feature is considered a blocker for Django 1.1, so I'm going to outline what the syntax for these aggregates will be.

To facillitate aggregates two new methods are being added to the queryset, aggregate and annotate.  Aggregate is used to preform basic aggregation on queryset itself, for example getting the MAX, MIN, AVG, COUNT, and SUM for a given field on the model.   Annotate is used for getting information about a related model.

For example, if we had a product model with a price field, we could get the max and minimum price for a product by doing the following:

.. sourcecode:: python
    
    Product.objects.aggregate(Min('price'), Max('price'))

this will return something like this:

.. sourcecode:: python
    
    {'price__min': 23.45,
     'price__max': 47.89,
    }

We can also give the results aliases, so it's easier to read(if no alias is provided it fallsback to using fieldname__aggregate:

.. sourcecode:: python
    
    Product.objects.aggregate(max_price = Max('price'), min_price = Min('price'))
    {'min_price': 23.45,
     'max_price': 47.89,
    }

You can also do aggregate queries on related fields, but the idea is the same, return a single value for each aggregate.

In my opinion, annotate queries are far more interesting.  Annotate queries let us represent queries such as, "give me all of the Tags that more than 3 objects have been tagged with", which would look like:

.. sourcecode:: python
    
    Tag.objects.annotate(num_items=Count('tagged')).filter(num_items__gt=3)

This would return a normal queryset where each Tag object has an attribute named num_items, that was the Count() of all of tagged for it(I'm assuming tagged is a reverse foreign key, to a model that represents a tagged relationship).  Another query we might want to execute would be to see how many awards authors of each author's publisher had won, this would look like:

.. sourcecode:: python
    
    Author.objects.annotate(num_publisher_awards=Count('publisher__authors__awards')).order_by('num_publisher_awards')

This is a little more complicated, but just like when using filter() we can chain this __ syntax.  Also, as you've probably noticed we can filter and order_by these annotated attributes the same as we can with regular fields.

If you're interested in seeing more of how this works, Nicolas Lara has written some documentation and doc tests that you can see `here <http://code.google.com/p/django-aggregation/w/list>`_.  For now none of this is in the Django source tree yet, but there is a patch with the latest work on `ticket 366 <http://code.djangoproject.com/ticket/3566>`_.

Happy thanksgiving!

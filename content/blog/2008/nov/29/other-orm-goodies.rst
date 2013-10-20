
Other ORM Goodies
=================


In addition to the aggregate work, the GSOC student had time to finish `ticket 7210 <http://code.djangoproject.com/ticket/7210>`_, which adds support for expressions to filter() and update().  This means you'll be able to execute queries in the form of:

.. sourcecode:: sql
    
    SELECT * FROM table WHERE height > width;

or similar UPDATE queries.  This has a syntax similar to that of Q objects, using a new F object.  So the above query would look like:

.. sourcecode:: python
    
    Model.objects.filter(height__gt=F('width'))

or an update query could look like:

.. sourcecode:: python
    
    Employee.objects.update(salary=F('salary')*1.1)

these objects support the full range of arithmetic operations.  These are slated to be a part of Django 1.1.

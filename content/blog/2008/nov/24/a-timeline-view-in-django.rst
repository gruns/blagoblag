
A timeline view in Django
=========================

:tags: django, models, orm, python, tips

One thing a lot of people want to do in Django is to have a timeline view, that shows all the objects of a given set of models ordered by a common key.  Unfortunately the Django ORM doesn't have a way of representing this type of query.  There are a few techniques people use to solve this.  One is to have all of the models inherit from a common baseclass that stores all the common information, and has a method to get the actual object.  The problem with this is that it could execute either O(N) or O(N*k) queries, where N is the number of items and k is the number of models.  It's N if your baseclass has the subtype it is stored on it, in which case you can directly grab it, else it's N*k since you have to try each type.  Another approach is to use a generic relation, this will also need O(N) queries since you need to get the related object for each generic one.  However, there's a better solution.

What we can do is use get a queryset for each of the models we want to display(O(k) queries), sorted on the correct key, and then use a simple merge to combine all of these querysets into a single list, comparing on a given key.  While this technically may do more operations than the other methods, it does fewer database queries, and this is often the most difficult portion of your application to scale.

Let's say we have 3 models, new tickets, changesets, and wikipage edits(what you see in a typical Trac install).  We can get our querysets and then merge them like so:

.. sourcecode:: python
    
    def my_view(request):
       tickets = Ticket.objects.order_by('create_date')
       wikis = WikiEdit.objects.order_by('create_date')
       changesets = Changeset.objects.order_by('create_date')
       objs = merge(tickets, wikis, changesets, field='create_date')
       return render_to_response('my_app/template.html', {'objects': objs})

Now we just need to write our merge function:

.. sourcecode:: python
    
    def merge_lists(left, right, field=None):
        i, j = 0, 0
        result = []
        while i:
            if getattr(left[i], field):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def merge(*querysets, **kwargs):
        field = kwargs.pop('field')
        if field is None:
            raise TypeError('you need to provide a key to do comparisons on')
        if len(querysets) == 1:
            return querysets[0]
    
        qs = [list(x) for x in querysets]
        q1, q2 = qs.pop(), qs.pop()
        result = merge_lists(q1, q2, field)
        for q in qs:
            result = merge_lists(result, q)
        return result

There might be a more efficient way to write our merge function, but for now it merges together an arbitrary number of querysets on a given key.

And that's all their is too it.  If you see a good way to make the merge function more efficient let me know, I would have liked to use Python's included heapq module, but it doesn't have a way to use a custom comparison function that I saw.

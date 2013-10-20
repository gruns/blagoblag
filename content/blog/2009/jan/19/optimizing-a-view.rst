
Optimizing a View
=================

:tags: compile, django, models, orm, python

Lately I've been playing with a bit of a fun side project.  I have about a year and half worth of my own chatlogs with friends(and 65,000 messages total) and I've been playing around with them to find interesting statistics.  One facet of my communication with my friends is that we link each other lots of things, and we can always tell when someone is linking something that we've already seen.  So I decided an interesting bit of information would be to see who is the worst offender.

So we want to write a function that returns the number of items each person has relinked, excluding items they themselves linked.  So I started off with the most simple implementation I could, and this was the end result:


.. sourcecode:: python
    
    from collections import defaultdict
    from operator import itemgetter
    
    from django.utils.html import word_split_re
    
    from logger.models import Message
    
    def calculate_relinks():
        """
        Calculate the number of times each individual has linked something that was
        linked previously in the course of the chat.
        """
        links = defaultdict(int)
        for message in Message.objects.all().order_by('-time').iterator():
            words = word_split_re.split(message.message)
            for word in words:
                if word.startswith('http'):
                    if Message.objects.filter(time__lt=message.time).filter(message__contains=word).exclude(speaker=message.speaker).count():
                        links[message.speaker] += 1
        links = sorted(links.iteritems(), key=itemgetter(1), reverse=True)
        return links

Here I iterated over the messages and for each one I went through each of the words and if any of them started with http(the definition of a link for my purposes) I checked to see if this had ever been linked before by someone other than the author of the current message.

This took about 4 minutes to execute on my dataset, it also executed about 10,000 SQL queries.  This is clearly unacceptable, you can't have a view that takes that long to render, or hits your DB that hard.  Even with aggressive caching this would have been unmaintainable.  Further this algorithm is O(n**2) or thereabouts so as my dataset grows this would have gotten worse exponentially.

By changing this around however I was able to achieve far better results:


.. sourcecode:: python
    
    from collections import defaultdict
    from operator import itemgetter
    
    from django.utils.html import word_split_re
    
    from logger.models import Message
    
    def calculate_relinks():
        """
        Calculate the number of times each individual has linked something that was
        linked previously in the course of the chat.
        """
        links = defaultdict(set)
        counts = defaultdict(int)
        for message in Message.objects.all().filter(message__contains="http").order_by('time').iterator():
            words = word_split_re.split(message.message)
            for word in words:
                if word.startswith('http'):
                    if any([word in links[speaker] for speaker in links if speaker != message.speaker]):
                        counts[message.speaker] += 1
                    links[message.speaker].add(word)
        counts = sorted(counts.iteritems(), key=itemgetter(1), reverse=True)
        return counts

Here what I do is go through each of the messages which contain the string "http"(this is already a huge advantage since that means we process about 1/6 of the messages in Python that we originally were), for each message we go through each of the words in it, and for each that is a link we check if any other person has said it by looking in the caches we maintain in Python, and if they do we increment their count, finally we add the link to that persons cache.

By comparison this executes in .3 seconds, executes only 1 SQL query, and it will scale linearly(as well as is possible).  For reference both of these functions are compiled using Cython.  This ultimately takes almost no work to do and for computationally heavy operations this can provide a huge boon.

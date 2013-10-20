
ORM Panel Recap
===============


Having now completed what I thought was a quite successful panel I thought it would be nice to do a review of some of the decisions I made, that some people had been asking about.  For those who missed it you can find a live blog of the event by James Bennett at `his blog <http://www.b-list.org/weblog/2009/mar/28/pycon-orm-panel/>`_, and a video should hopefully be going up sometime soon.

Why Google App Engine
---------------------

As Guido pointed out App Engine does not have an ORM, as App Engine doesn't have a relational datastore.  However, it does have something that looks and acts quite a lot like other ORMs, and it does fundamentally try to serve the same purpose, offering a persistence layer.  Therefore I decided it was at least in the same class of items I wanted to add.  Further, with the rise of non-relational DBs that all fundamentally deal with the same issues as App Engine, and the relationship between ORMs and these new persistence layers I thought it would be advantageous to have one of these, Guido is a knowledgeable and interesting person, and that's how the cookie crumbled.

Why Not ZODB/Storm/A Talking Pony
---------------------------------

Time.  I would have loved to have as many different ORMs/things like them as exist in the Python eco-sphere, but there just wasn't time.  We had 55 minutes to present and as it is that wasn't enough.  I ultimately had time to ask 3 questions(one of which was just background), plus 5 shorter audience questions. I was forced to cut out several questions I wanted to ask, but didn't have time to, for those who are interested the major questions I would have liked to ask
were:

 * What most often requested feature won't you add to your ORM?
 * What is the connection between an ORM and a schema migration tool.  Should they both be part of the same project, should they be tied together, or are they totally orthogonal?
 * What's your support for geographic data?  Is this(or other complex data types like it) in scope for the core of an ORM?

Despite these difficulties I thought the panel turned out very well.  If there are any other questions about why things were the way they were just ask in the comments and I'll try to post a response.

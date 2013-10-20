
A Few More Thoughts on the Identity Mapper
==========================================

:tags: django, foreignkey, internals, models, orm

It's late, and I've my flight was delayed for several hours so today is going to be another quick post.  With that note here are a few thoughts on the identity mapper:
 * We can optimize it to actually execute fewer queries by having it run the query as usual, and then use the primary key to check the cache, else cache the instance we already have.
 * As Doug points out in the comments, there are built in caching utilities in Django we should probably be taking advantage of.  The only qualification is that whatever cache we use needs to be in memory and in process.
 * The cache is actually going to be more efficient than I originally thought.  On a review of the source the default manager is used for some related queries, so our manager will actually be used for those.
 * The next place to optimize will actually be on single related objects(foreign keys and one to ones).  That's because we already have their primary key and so we can check for them in the cache without executing any SQL queries.

And lastly a small note.  As you may have noticed I've been doing the National Blog Everyday for a Month Month, since I started two days late, I'm going to be continueing on for another two days.

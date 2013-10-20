
Why Meta.using was removed
==========================

:tags: django, gsoc, models, orm, python

Recently Russell Keith-Magee and I decided that the Meta.using option needed to be removed from the multiple-db work on Django, and so we did.  Yesterday someone tweeted that this change caught them off guard, so I wanted to provide a bit of explanation as to why we made that change.

The first thing to note is that Meta.using was very good for one specific use case, horizontal partitioning by model.  Meta.using allowed you to tie a specific model to a specific database by default.  This meant that if you wanted to do things like have users be in one db and votes in another this was basically trivial.  Making this use case this simple was definitely a good thing.

The downside was that this solution was very poorly designed, particularly in light on Django's reusable application philosophy.  Django emphasizes the reusability of application, and having the Meta.using option tied your partitioning logic to your models, it also meant that if you wanted to partition a reusable application onto another DB this easily the solution was to go in and edit the source for the reusable application.  Because of this we had to go in search of a better solution.

The better solution we've come up with is having some sort of callback you can define that lets you decide what database each query should be executed on.  This would let you do simple things like direct all queries on a given model to a specific database, as well as more complex sharding logic like sending queries to the right database depending on which primary key value the lookup is by.  We haven't figured out the exact API for this, and as such this probably won't land in time for 1.2, however it's better to have the right solution that has to wait than to implement a bad API that would become deprecated in the very next release.


That's not change we can believe in
===================================

:tags: django, obama, php, python

Yesterday president-elect Obama's campaign unveiled their transitional website, `change.gov <http://www.change.gov/>`_.  So, as someone who's interested in these things I immediately began to look at what language, framework, or software package they were using.  The first thing I saw was that they were using Apache, however beyond that there were no distinctive headers.  None of the pages had tell-tale extensions like .php or .aspx.  However, one thing that struck me was that most pages were at a url in the form of /page/\*/, which is the same format of the Obama campaign website, which I knew was powered by Blue State Digital's CMS.  On the Obama campaign's site however, there were a few pages with those tell-tale .php extension, so I've come to the conclusion that the new site also uses PHP.  And to that I say, that's not change we can believe in.

PHP has been something of a powerhouse in web development for the last few years, noted for it's ease of deployment and quick startup times, it's drawn in legions of new users.  However, PHP has several notable flaws.  Firstly, it doesn't encourage best practices, ranging from things like code organization (PHP currently has no concept of namespaces), to database security (the included mysql database adapter doesn't feature parameterized queries), and beyond.  However, this isn't just another post to bash on PHP (as much as I'd like to do one), there are already plenty of those out there.  This post is instead to offer some of the benefits of switching, to Python, or Ruby, or whatever else.

 * You develop faster. Using a framework like Django, or Rails, or TurboGears let's you do things very quickly.
 * You get the benefits of the community, with Django you get all the reusable applications, Rails has plugins, TurboGears has middleware. Things like these quite simply don't exist in the PHP world.
 * You get a philosophy. As far as I can tell, PHP has no philosophy, however both Python and Ruby do, and so do their respective frameworks. Working within a consistant philsophy makes development remarkably more sane.

If you currently are a user of PHP, I beg of you, take a chance, try out Ruby or Python, or whatever else. Give Django, or TurboGears, or Rails a shot. Even if you don't end up liking it, or switching, it's worth giving it a shot.

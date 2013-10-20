
Hot Django on WSGI Action (announcing django-wsgi)
==================================================

:tags: django, python, release, wsgi

For a long time it's been possible to deploy a Django project under a WSGI server, and in the run up to Django's 1.0 release a number of bugs were fixed to make Django's WSGI handler as compliant to the `standard <http://www.python.org/dev/peps/pep-0333/>`_ as possible.  However, Django's support for interacting with the world of WSGI application, middleware, and frameworks has been less than stellar.  However, I recently got inspired to improve this situation.

WSGI (Web Server Gateway Interface) is a specification for how applications and frameworks in Python can interface with a server.  There are tons of servers that support the WSGI interface, most notably ``mod_wsgi`` (an Apache plugin), however there are tons of other ones, ``spawning``, ``twisted``, ``uwsgi``, ``gunicorn``, ``cherrypy``, and probably dozens more.

The inspiration for improving Django's integration with the WSGI world was Ruby on Rails 3's improved support for ``Rack``, ``Rack`` is the Ruby world's equivilant to WSGI.  In Rails 3 every layer of the stack, the entire application, the dispatch, and individual controllers, is exposed as a Rack application.  It occured to me that it would be pretty swell if we could do the same thing with Django, allow individual views and URLConfs to be exposed as WSGI application, *and* the reverse, allowing WSGI application to be deployed inside of Django application (via the standard URLConf mapping system).  Another part of this inspiration was discussing `gunicorn <http://github.com/benoitc/gunicorn>`_ with `Eric Florenzano <http://www.eflorenzano.com/>`_, gunicorn is an awesome new WSGI server, inspired by Ruby's `Unicorn <http://unicorn.bogomips.org/>`_, there's not enough space in this post to cover all the reasons it is awesome, but it is.

The end result of this is a new package, `django-wsgi <http://github.com/alex/django-wsgi>`_, which aims to bridge the gap between the WSGI world and the Django world.  Here's an example of exposing a Django view as a WSGI application:

.. sourcecode:: python
    
    from django.http import HttpResponse
    
    from django_wsgi import wsgi_application
    
    def my_view(request):
        return HttpResponse("Hello world, I'm a WSGI application!")
    
    
    application = wsgi_application(my_view)


And now you can point any WSGI server at this and it'll serve it up for you.  You can do the same thign with a URLConf:

.. sourcecode:: python
    
    from django.conf.urls.defaults import patterns
    from django.http import HttpResponse
    
    from django_wsgi import wsgi_application
    
    def hello_world(request):
        return HttpResponse("Hello world!")
    
    def hello_you(request, name):
        return HttpResponse("Hello %s!" % name)
    
    
    urls = patterns("",
        (r"^$", hello_world),
        (r"^(?P<name>\w+)/$", hello_you)
    )
    
    application = wsgi_application(urls)


Again all you need to do is point your server at this and it just works.  However, the point of all this isn't just to make building single file applications easier (although this definitely does), the real win is that you can take a Django application and mount it inside of another WSGI application through whatever process it supports.  Of course you can also go the other direction, mount a WSGI application inside of a Django URLconf:

.. sourcecode:: python
    
    from django.conf.urls.defaults import *
    
    from django_wsgi import django_view
    
    def my_wsgi_app(environ, start_response):
        start_response("200 OK", [("Content-type", "text/plain")])
        return ["Hello World!"]
    
    urlpatterns = patterns("",
        # other views here
        url("^my_view/$", django_view(my_wsgi_app))
    )


And that's all there is to it.  Write your apps the way you want and deploy them, plug them in to each other, whatever.  There's a lot of work being done in the Django world to play nicer with the rest of the Python ecosystem, and that's definitely a good thing.  I'd also like to thank `Armin Ronacher <http://lucumr.pocoo.org/>`_ for helping me make sure this actually implements WSGI correctly.  Please use this, fork it, send me hate mail, improve it, and enjoy it!

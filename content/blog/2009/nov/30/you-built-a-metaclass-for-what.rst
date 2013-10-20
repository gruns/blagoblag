
You Built a Metaclass for *what*?
=================================


Recently I had a bit of an interesting problem, I needed to define a way to represent a C++ API in Python.  So, I figured the best way to represent that was one class in Python for each class in C++, with a functions dictionary to track each of the methods on each class.  Seems simple enough right, do something like this:

.. sourcecode:: python
    
        class String(object):
            functions = {
                "size": Function(Integer, []),
            }

We've got a String class with a functions dictionary that maps method names to Function objects.  The Function constructor takes a return type and a list of arguments.  Unfortunately we run into a problem when we want to do something like this:

.. sourcecode:: python
    
        class String(object):
            functions = {
                "size": Function(Integer, []),
                "append": Function(None, [String])
            }

If we try to run this code we're going to get a NameError, String isn't defined yet.  Django models have a similar issue, with recursive foreign keys.  Django's solution is to use the placeholder string "self", and have a metaclass translate it into the right class.  Also having a slightly more declarative API might be nice, so something like this:

.. sourcecode:: python
    
        class String(DeclarativeObject):
            size = Function(Integer, [])
            append = Function(None, ["self"])

So now that we have a nice pretty API we need our metaclass to make it happen:

.. sourcecode:: python
    
        RECURSIVE_TYPE_CONSTANT = "self"
    
        class DeclarativeObjectMetaclass(type):
            def __new__(cls, name, bases, attrs):
                functions = dict([(n, attr) for n, attr in attrs.iteritems()
                    if isinstance(attr, Function)])
                for attr in functions:
                    attrs.pop(attr)
                new_cls = super(DeclarativeObjectMetaclass, cls).__new__(cls, name, bases, attrs)
                new_cls.functions = {}
                for name, function in functions.iteritems():
                    if function.return_type == RECURSIVE_TYPE_CONSTANT:
                        function.return_type = new_cls
                    for i, argument in enumerate(function.arguments):
                        if argument == RECURSIVE_TYPE_CONSTANT:
                            function.arguments[i] = new_cls
                    new_cls.functions[name] = function
                return new_cls
    
        class DeclarativeObject(object):
            __metaclass__ = DeclarativeObjectMetaclass
    

And that's all their is to it.  We take each of the functions on the class out of the attributes, create a normal class instance without the functions, and then we do the replacements on the function objects and stick them in a functions dictionary.

Simple patterns like this can be used to build beautiful APIs, as is seen in Django with the models and forms API.

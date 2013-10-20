
MultiMethods for Python 
========================


Every once and a while the topic of multimethods (also known as generic dispatch) comes up in the Python world (see `here <http://www.python.org/dev/peps/pep-3124/>`_, `and here <http://mike.axiak.net/blog/2010/06/25/python-generic-dispatch/>`_, `here too <http://www.artima.com/weblogs/viewpost.jsp?thread=101605>`_, `and finally here <http://twitter.com/gutworth/status/9750313767>`_, and probably others).  For those of you who aren't familiar with the concept, the idea is that you declare a bunch of functions with the same name, but that take different arguments and the language routes your calls to that function to the correct implementation, based on what types you're calling it with.  For example here's a C++ example:

.. sourcecode:: c++
    
    #include <iostream>
    
    void special(int k) {
        std::cout << "I AM THE ALLMIGHTY INTEGER " << k << std::endl;
    }
    
    void special(std::string k) {
        std::cout << "I AM THE ALLMIGHTY STRING " << k << std::endl;
    }
    
    int main() {
        special(42);
        special("magic");
        return 0;
    }

As you can probably guess this will print out::
    
    I AM THE ALLMIGHTY INTEGER 3
    I AM THE ALLMIGHTY STRING magic


You, the insightful reader, are no doubt fuming in your seats now, "Alex, you idiot, Python functions don't have type signatures, how can we route our calls based on something that does not exist!", and right you are.  However, don't tell me you've never written a function that looks like:

.. sourcecode:: python
    
    def my_magic_function(o):
        if isinstance(o, basestring):
            return my_magic_function(int(o))
        elif isinstance(o, (int, long)):
            return cache[o]
        else:
            return o

Or something like that, the point is you have one function that has a couple of different behaviors based on the type of it's parameter.  Perhaps it'd be nice to separate each of those behaviors into their own function (or not, I don't really care what you do).

I was saying that a bunch of people have already implemented these, why am I?  Mostly for fun (that's still a valid reason, right?), but also because a bunch of the implementations make me sad.  Some of them use crazy hacks (reading up through stack frames), a few of them have global registrys, and all of them rely on the name of the function to identify a single "function" to be overloaded.  However, they also all have one good thing in common: decorators, yay!

My implementation is pretty simple, so I'll present it, and it's test suite without explanation:

.. sourcecode:: python
    
    class MultiMethod(object):
        def __init__(self):
            self._implementations = {}
        
        def _get_predicate(self, o):
            if isinstance(o, type):
                return lambda x: isinstance(x, o)
            assert callable(o)
            return o
        
        def register(self, *args, **kwargs):
            def inner(f):
                key = (
                    args,
                    tuple(kwargs.items()),
                )
                if key in self._implementations:
                    raise TypeError("Duplicate registration for %r" % key)
                self._implementations[key] = f
                return self
            return inner
        
        def __call__(self, *args, **kwargs):
            for spec, func in self._implementations.iteritems():
                arg_spec, kwarg_spec = spec
                kwarg_spec = dict(kwarg_spec)
                if len(args) != len(arg_spec) or set(kwargs) != set(kwarg_spec):
                    continue
                if (all(self._get_predicate(spec)(arg) for spec, arg in zip(arg_spec, args)) and
                    all(self._get_predicate(spec)(kwargs[k]) for k, spec in kwarg_spec.iteritems())):
                    return func(*args, **kwargs)
            raise TypeError("No implementation with a spec matching: %r, %r" % (
                args, kwargs))


And the tests:

.. sourcecode:: python
    
    import unittest2 as unittest

    from multimethod import MultiMethod


    class MultiMethodTestCase(unittest.TestCase):
        def test_basic(self):
            items = MultiMethod()
            
            @items.register(list)
            def items(l):
                return l
            
            @items.register(dict)
            def items(d):
                return d.items()
            
            self.assertEqual(items([1, 2, 3]), [1, 2, 3])
            # TODO: dict ordering dependent, 1 item dict?
            self.assertEqual(items({"a": 1, "b": 2}), [("a", 1), ("b", 2)])
            
            with self.assertRaises(TypeError):
                items(xrange(3))
        
        def test_duplicate(self):
            m = MultiMethod()
            
            @m.register(list)
            def m(o):
                return o
            
            with self.assertRaises(TypeError):
                @m.register(list)
                def m(o):
                    return o


    if __name__ == "__main__":
        unittest.main()


Bon appÃ©tit.

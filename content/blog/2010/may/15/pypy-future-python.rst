
PyPy is the Future of Python 
=============================

:tags: pypy, python

Currently the most common implementation of Python is known as CPython, and it's the version of Python you get at `python.org <http://python.org>`_, probably 99.9% of Python developers are using it.  However, I think over the next couple of years we're going to see a move away from this towards PyPy, Python written in Python.  This is going to happen because PyPy offers better speed, more flexibility, and is a better platform for Python's growth, and the most important thing is you can make this transition happen.

The first thing to consider: speed.  PyPy is a lot faster than CPython for a lot of tasks, and they've got `the benchmarks to prove it <http://speed.pypy.org/overview/>`_.  There's room for improvement, but it's clear that for a lot of benchmarks PyPy screams, and it's not just number crunching (although PyPy is good at that too).  Although Python performance might not be a bottleneck for a lot of us (especially us web developers who like to push performance down the stack to our database), would you say no to having your code run 2x faster?

The next factor is the flexibility.  By writing their interpreter in RPython PyPy can automatically generate C code (like CPython), but also JVM and .NET versions of the interpreter.  Instead of writing entirely separate Jython and IronPython implementations of Python, just automatically generate them from one shared codebase.  PyPy can also have its binary generated with a stackless option, just like stackless Python, again no separate implementations to maintain.  Lastly, PyPy's JIT is almost totally separate from the interpreter, this means changes to the language itself can be made without needing to update the JIT, contrast this with many JITs that need to statically define fast-paths for various operations.

And finally that it's a better platform for growth.  The last point is a good example of this: one can keep the speed from the JIT while making changes to the language, you don't need to be an assembly expert to write a new bytecode, or play with the builtin types, the JIT generator takes care of it for you.  Also, it's written in Python, it may be RPython which isn't as high level as regular Python, but compare the implementations of of ``map`` from CPython and PyPy:

.. sourcecode:: c

    static PyObject *
    builtin_map(PyObject *self, PyObject *args)
    {
        typedef struct {
            PyObject *it;           /* the iterator object */
            int saw_StopIteration;  /* bool:  did the iterator end? */
        } sequence;

        PyObject *func, *result;
        sequence *seqs = NULL, *sqp;
        Py_ssize_t n, len;
        register int i, j;

        n = PyTuple_Size(args);
        if (n < 2) {
            PyErr_SetString(PyExc_TypeError,
                            "map() requires at least two args");
            return NULL;
        }

        func = PyTuple_GetItem(args, 0);
        n--;

        if (func == Py_None) {
            if (PyErr_WarnPy3k("map(None, ...) not supported in 3.x; "
                               "use list(...)", 1) < 0)
                return NULL;
            if (n == 1) {
                /* map(None, S) is the same as list(S). */
                return PySequence_List(PyTuple_GetItem(args, 1));
            }
        }

        /* Get space for sequence descriptors.  Must NULL out the iterator
         * pointers so that jumping to Fail_2 later doesn't see trash.
         */
        if ((seqs = PyMem_NEW(sequence, n)) == NULL) {
            PyErr_NoMemory();
            return NULL;
        }
        for (i = 0; i < n; ++i) {
            seqs[i].it = (PyObject*)NULL;
            seqs[i].saw_StopIteration = 0;
        }

        /* Do a first pass to obtain iterators for the arguments, and set len
         * to the largest of their lengths.
         */
        len = 0;
        for (i = 0, sqp = seqs; i < n; ++i, ++sqp) {
            PyObject *curseq;
            Py_ssize_t curlen;

            /* Get iterator. */
            curseq = PyTuple_GetItem(args, i+1);
            sqp->it = PyObject_GetIter(curseq);
            if (sqp->it == NULL) {
                static char errmsg[] =
                    "argument %d to map() must support iteration";
                char errbuf[sizeof(errmsg) + 25];
                PyOS_snprintf(errbuf, sizeof(errbuf), errmsg, i+2);
                PyErr_SetString(PyExc_TypeError, errbuf);
                goto Fail_2;
            }

            /* Update len. */
            curlen = _PyObject_LengthHint(curseq, 8);
            if (curlen > len)
                len = curlen;
        }

        /* Get space for the result list. */
        if ((result = (PyObject *) PyList_New(len)) == NULL)
            goto Fail_2;

        /* Iterate over the sequences until all have stopped. */
        for (i = 0; ; ++i) {
            PyObject *alist, *item=NULL, *value;
            int numactive = 0;

            if (func == Py_None && n == 1)
                alist = NULL;
            else if ((alist = PyTuple_New(n)) == NULL)
                goto Fail_1;

            for (j = 0, sqp = seqs; j < n; ++j, ++sqp) {
                if (sqp->saw_StopIteration) {
                    Py_INCREF(Py_None);
                    item = Py_None;
                }
                else {
                    item = PyIter_Next(sqp->it);
                    if (item)
                        ++numactive;
                    else {
                        if (PyErr_Occurred()) {
                            Py_XDECREF(alist);
                            goto Fail_1;
                        }
                        Py_INCREF(Py_None);
                        item = Py_None;
                        sqp->saw_StopIteration = 1;
                    }
                }
                if (alist)
                    PyTuple_SET_ITEM(alist, j, item);
                else
                    break;
            }

            if (!alist)
                alist = item;

            if (numactive == 0) {
                Py_DECREF(alist);
                break;
            }

            if (func == Py_None)
                value = alist;
            else {
                value = PyEval_CallObject(func, alist);
                Py_DECREF(alist);
                if (value == NULL)
                    goto Fail_1;
            }
            if (i >= len) {
                int status = PyList_Append(result, value);
                Py_DECREF(value);
                if (status < 0)
                    goto Fail_1;
            }
            else if (PyList_SetItem(result, i, value) < 0)
                goto Fail_1;
        }

        if (i < len && PyList_SetSlice(result, i, len, NULL) < 0)
            goto Fail_1;

        goto Succeed;

    Fail_1:
        Py_DECREF(result);
    Fail_2:
        result = NULL;
    Succeed:
        assert(seqs);
        for (i = 0; i < n; ++i)
            Py_XDECREF(seqs[i].it);
        PyMem_DEL(seqs);
        return result;
    }


That's a lot of code!  It wouldn't be bad, for C code, except for the fact that there's far too much boilerplate: every single call into the C-API needs to check for an exception, and ``INCREF`` and ``DECREF`` calls are littered throughout the code.  Compare this with PyPy's RPython implementation:

.. sourcecode:: python

    def map(space, w_func, collections_w):
        """does 3 separate things, hence this enormous docstring.
           1.  if function is None, return a list of tuples, each with one
               item from each collection.  If the collections have different
               lengths,  shorter ones are padded with None.

           2.  if function is not None, and there is only one collection,
               apply function to every item in the collection and return a
               list of the results.

           3.  if function is not None, and there are several collections,
               repeatedly call the function with one argument from each
               collection.  If the collections have different lengths,
               shorter ones are padded with None
        """
        if not collections_w:
            msg = "map() requires at least two arguments"
            raise OperationError(space.w_TypeError, space.wrap(msg))
        num_collections = len(collections_w)
        none_func = space.is_w(w_func, space.w_None)
        if none_func and num_collections == 1:
            return space.call_function(space.w_list, collections_w[0])
        result_w = []
        iterators_w = [space.iter(w_seq) for w_seq in collections_w]
        num_iterators = len(iterators_w)
        while True:
            cont = False
            args_w = [space.w_None] * num_iterators
            for i in range(len(iterators_w)):
                try:
                    args_w[i] = space.next(iterators_w[i])
                except OperationError, e:
                    if not e.match(space, space.w_StopIteration):
                        raise
                else:
                    cont = True
            w_args = space.newtuple(args_w)
            if cont:
                if none_func:
                    result_w.append(w_args)
                else:
                    w_res = space.call(w_func, w_args)
                    result_w.append(w_res)
            else:
                return space.newlist(result_w)
    map.unwrap_spec = [ObjSpace, W_Root, "args_w"]


It's not exactly what you'd write for a pure Python implementation of ``map``, but it's a hell of a lot closer than the C version.

The case for PyPy being the future is strong, I think, however it's not all sunshine are roses, there are a few issues.  It lags behind CPython's version (right now Python 2.5 is implemented), C extension compatibility isn't there yet, and not enough people are trying it out yet.  But PyPy is getting there, and you can help.

Right now the single biggest way to help for most people is to test their code.  Any pure Python code targeting Python 2.5 should run perfectly under PyPy, and if it doesn't: it's a bug, if it's slower than Python: let us know (unless it involves ``re``, we know it's slow).  Maybe try out your C-extensions, however ``cpyext`` is very alpha and even a segfault isn't surprising (but let us know so we can investigate).  Of course help on development is always appreciated, right now most of the effort is going into speeding up the JIT even more, however I believe there is also going to be work on moving up to Python 2.7 (currently pre-release) this summer.  If you're interested in helping out with either you should hop into `#pypy on irc.freenode.net <irc://irc.feenode.net#pypy>`_, or send a message to `pypy-dev <http://codespeak.net/mailman/listinfo/pypy-dev>`_.  PyPy's doing good work, Python doesn't need to be slow, and we don't all need to write C code!

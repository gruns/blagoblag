
Disambiguating BSON and msgpack
===============================

:tags: programming, python

I had a fairly fun project at work recently, so I thought I'd write about it.
We currently store `BSON`_ blobs of data in many places. This is unfortunate,
because BSON is bloated and slow (an array is internally stored as a dictionary
mapping the strings ``"0"``, ``"1"``, ``"2"``, etc. to values). So we wanted to
migrate to `msgpack`_, which I've measured as requiring 46% of the space of
BSON, and being significantly faster to deserialize (we aren't concerned with
serialization speed, though I'm relatively confident that's faster as well).

The one trick we wanted to pull was to do the migration in place, that is
gradually rewrite all the columns' data from BSON to msgpack. This is only
possible if the data can be interpreted as one or the other unambiguously. So I
was tasked if finding out if this was possible.

The first thing that's important to know about BSON is that the first 4-bytes
are the length of the entire document (in bytes) as a signed integer, little
endian. msgpack has no specific prefix, the first bytes are merely the typecode
for whatever the element is. At `Rdio`_, we know something about our data
though, because BSON requires all top-level elements to be dictionaries, and
we're just re-serializing the same data, we know that all of these msgpacks
will have dictionaries as the top level object.

Because a BSON blob starts with its size, in bytes, we're going to try to find
the smallest possible 4-byte starting sequence (interpreted as an integer) one
of our payloads could have, in order to determine what the smallest possible
ambiguity is.

So the first case is the empty dictionary, in msgpack this is serialized as:

.. sourcecode:: pycon

    >>> msgpack.packb({})
    '\x80'

That's less than 4 bytes, and all BSONs are at least 4 bytes, so that can't be
ambiguous. Now let's look at a dictionary with some content. Another thing we
know about our payloads is that all the keys in the dictionaries are strings,
and that the keys are alphanumeric or underscores. Looking at the
`msgpack spec`_, the smallest key (interpreted as its serialized integer value)
that could exist is ``"0"``, since ``"0"`` has the lowest ASCII value of any
letter, number, or underscore. Further, from the `msgpack spec`_ we know that
the number ``0`` serializes as a single byte, so that will be the key's value.
Let's see where this gets us:

.. sourcecode:: pycon

    >>> msgpack.packb({"0": 0})
    '\x81\xa10\x00'

A 4 byte result, perfect, this is the smallest prefix we can generate, let's
see how many bytes this would be:

.. sourcecode:: pycon

    >>> struct.unpack('<l', '\x81\xa10\x00')
    (3187073,)

3187073 bytes, or a little over 3 MB. To be honest I'm not sure we have a key
that starts with a number, let's try with the key ``"a"``:

.. sourcecode:: pycon

    >>> msgpack.packb({"a": 0})
    '\x81\xa1a\x00'
    >>> struct.unpack('<l', '\x81\xa1a\x00')
    (6398337,)

A little over 6 MB. Since I know that none of the payloads we store are
anywhere close to this large, we can safely store either serialization format,
and be able to interpret the result unambiguously as one or the other.

So our final detection code looks like:

.. sourcecode:: python

    def deserialize(s):
        if len(s) >= 4 and struct.unpack('<l', s[:4])[0] == len(s):
            return BSON(s).decode()
        else:
            return msgpack.unpackb(s)

If this sounds like a fun kind of the thing to do, you should
`apply to come work with me at Rdio`_.

.. _`BSON`: http://bsonspec.org/
.. _`msgpack`: http://msgpack.org/
.. _`Rdio`: http://www.rdio.com/
.. _`msgpack spec`: http://wiki.msgpack.org/display/MSGPACK/Format+specification
.. _`apply to come work with me at Rdio`: http://www.rdio.com/careers/

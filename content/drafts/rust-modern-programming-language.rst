Rust: A modern programming environment
======================================

I've been following along with `Rust`_ for quite a while. It's a pretty neat
language which offers the promise of the control (and performance) of C, with
unparalleled safety, protecting both against segfaults and against concurrency
bugs. I spent the weekend playing with Rust, and the thing that struck me most
was not the language itself, but how refreshing the tooling around Rust was.

Rust comes with a build and packaging system named `Cargo`_. I wish every
programming language had something like Cargo:

Cargo presents a consistent interface to building libraries and binaries, any
Rust project's source can be built with just ``cargo build``. It also provides
seemless integration with the package management system, to add a new dependency
all you need to do is add ``library = "version"`` to your build configuration
(``Cargo.toml``) and the next time you ``cargo build`` the library is installed
for you.

Cargo also provides a unified interface to testing, ``cargo test`` will build
your project and run the tests for it.

All these consistent UIs for doing basic tasks mean that Travis CI integration
is trivial. Just slap ``language: rust`` in your ``.travis.yml`` and you're
done.

Finally, Rust/Cargo make deployment easy by emitting statically linked
binraries. Simply ``cargo build --release`` and do what you want with the
binary, e.g. ``scp`` to your server and run.

Coming from the worlds of Python, Ruby, Java, or Go there's so much to love
here:

* No need to maintain explicit ``virtualenv``\ s, ``cargo build`` brings in the
  right dependencies for whatever you're building.
* No need to prefix everything with ``bundle exec``, you just invoke the binary
  you want.
* No smorgasbord of third-party solutions for managing library versions, Rust
  comes with a complete solution out of the box.
* No XML.

Working in Rust is refreshingly modern. Out of the box all the pieces you need
for a real software development environment are just there.

PS: Here's the `thing I made`_.

.. _`Rust`: http://www.rust-lang.org/
.. _`Cargo`: http://doc.crates.io/
.. _`thing I made`: https://github.com/alex/rust-asn1

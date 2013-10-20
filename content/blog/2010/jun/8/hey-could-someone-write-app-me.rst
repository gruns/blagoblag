
Hey, could someone write this app for me 
=========================================


While doing some work today I realized that generating fixtures in Django is way too much of a pain in the ass, and I suspect it's a pain in the ass for a lot of other people as well.  I also came up with an API I'd kind of like to see for it, unfortunately I don't really have the time to write the whole thing, however I'm hoping someone else does.

The key problem with writing fixtures is that you want to have a clean enviroment to generate them, and you need to be able to edit them in the future.  In addition, I'd personally prefer to have my fixture generation specifically be imperative.  I have an API I think I think solves all of these concerns.

Essentially, in every application you can have a ``fixture_gen.py`` file, which contains a bunch of functions that can generate fixtures:

.. sourcecode:: python
    
    from fixture_generator import fixture_generator
    
    from my_app.models import Model1, Model2
    
    
    @fixture_generator(Model1, Model2, requires=["my_app.other_dataset"])
    def some_dataset():
        # Some objects get created here
    
    @fixture_generator(Model1)
    def other_dataset():
        # Some objects get created here


Basically you have a bunch of functions, each of which is responsible for creating some objects that will become a fixture.  You then decorate them with a decorator that specifies what models need to be included in the fixture that results from them, and finally you can optionally specify dependencies (these are necessary because a dependency could use models which your fixture doesn't).

After you have these functions there's a management command which can be invoked to actually generate the fixtures:

.. sourcecode:: python

    $ ./manage.py generate_fixture my_app.some_dataset --format=json --indent=4


Which actually creates the clean database enviroment, handles the dependencies, calls the functions, and dumps the fixtures to ``stdout``.  Then you can redirect that ``stdout`` off to a file somewhere, for use in testing or whatever else people use fixtures for.

Hopefully someone else has this problem, and likes the API enough to build this.  Failing that I'll try to make some time for it, but no promises when (aka if you want it you should probably build it).


PyGTK and Multiprocessing
=========================


Yesterday was election day, and for many people that meant long nights following the results, waiting to see who would be declared the next president of the United States of America.  Politics is a game of numbers, and it's nice to offload the crunching to our computers.  I had written up a simple application for projecting win likelihood for the candidates based on the likelihood of a win in an individual state.  If you are interested in the application itself you can see it `here <http://github.com/alex/election-sim/tree/master>`_.  However this post is going to look at the new multiprocessing library, and how I used it with PyGTK.

Part of my application is that whenever you update a probability for a given candidate in a given state it recomputes their win percentage for the election as a whole.  To make this as accurate as possible it runs multiple simulations of the scenario to compute the win percentage.  Originally I was running these computations in the same thread as the GUI work and I found that I could only do about 250 simulations before it had a drastically negative impact on usability.  So the next step was to offload these calculations into another process.

To go about this I created an Updater class which is a subclass of multiprocessing.Process.  It takes a pipe as it's only argument, and it's run method just loops forever polling the pipe for new projection results, tabulating them, and then sending the projection back through the pipe.

In the main process the application obviously starts by creating a duplex pipe, spawning the second process (and giving it the pipe).  Then, using the facilities of the gobject library, it sets up a method that checks for new projection results and updates the GUI to be executed whenever the main thread is idle(gobject.idle_add).  And lastly the signal responder that gets called whenever the user changes some data simply marshals up the necessary data, and sets it through the pipe to the other process.

And that's all, in total I believe it was under 25 lines of code changed to make my application use a separate process for calculation.

Edit: Upon request, `this <http://github.com/alex/election-sim/commit/cc93df649d1295deab96f1f1ab1ff709e8b0f391>`_ is the diff where I made the original changes, several subsequent commits will better reflect what is described here though.

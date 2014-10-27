My Ideal Development Environment
================================

Here's what a day looks like in my ultimate development environment:

Get into the office on Monday morning at 9; I'm a big fan of working from an
office on a "normal" schedule (it's not important to me that everyone else do
this though).

I'll take a look at the issue tracker, and find the top priority outstanding
bug. I like to get started with a bug fix, rather than feature work, I couldn't
tell you why. Work on the bug for a while, and submit a pull request. No matter
how small the fix, it doesn't go directly to master.

Now the fix, plus tests of course, wait for code review. Submitting a PR
automatically triggers the CI system. It checks that tests pass, code passes
style checks, and that docs compile; I've already run all these locally of
course, but now the code review UI shows my team mates that everything is
green.

I get some feedback on the patch from a co-worker, maybe even more than one. I
do some polish work on the patch, and then resubmit it. Tests run, and pass,
and my coworker merges the patch, since it looks good to them now.

And now the magic starts. First, the CI runs again. This time, in addition to
running tests, it also creates a build artifact. Once the CI is done, the
deployment system takes the artifact and deploys to production.

For a few minutes, either myself or the person who performed the merge keeps
half our eye on the project's metrics and exception tracker; someone would be
paged if anything bad actually happened, but we want to be on top of it.

Now I'm properly warmed up for the day. Next I'll see if there's any patches
that need review, and do some code review. Once I've made sure none of my co-
workers are blocked waiting for a review, I'll go through open issues that need
design or architecture input, to contribute my 2 cents. Finally, I'll get back
to the feature I'm working on and try to make some progress.

After lunch, we'll have a weekly team meeting. Everyone will share their goals
for the week, we'll make sure everyone knows who is on-call for the week, and
the team lead will let us know if there's any new features or product changes
coming up on the horizon that we'll need to start planning for.

After the meeting (which took about 30 minutes), it's back to juggling code
review, working on my own patches, and giving and asking for design feedback on
open issues.

And that's my ideal development environment!

I often get questions on why various pieces of it are important to me, so I'll
try to explain.

I've `previous written about why code review is important to me`_. It's really
the bedrock of the workflow, everything goes through code review before it hits
production.

The point that often gets the most push back is the continuous deployment. Many
folks hear that and think, "Won't you be deploying tons of bugs to
production?!?" The answer is: yes, we will deploy bugs to production. If you're
deploying less frequently, you're still going to be deploying bugs. You don't
spend nearly enough time or money to be bug free. Instead the focus is on, how
do we minimize the impact of bugs.

Deploying in smaller increments makes deployment safer because it the unit of
deployment is easier to audit, and because it makes identifying the bad commit
easier. It also makes rollbacks easier. Moreover, it makes developers happier,
first by reducing the stress that comes with unsafe deployments, and also by
removing the wait to get your patch in production,. It also puts automation at
the forefront, making it easier to maintain the system.

Next is the issue tracker. The issue tracker is the source of truth for any
tasks that need to be accomplished by the team. It's used to express
dependencies, and folks can always look at it to find work they need to do.
Tasks are decomposed as much as possible into units of work that can be
executed. For example a task might look like:

* Add the new feature

  * Design the needed API endpoints

    * Write documentation for the API
  * Front end work

    * Convert mockups to HTML/CSS
    * Develop JavaScript
  * Back end end work

    * Design new models
    * Develop domain logic
    * Develop APIs
  * Ops

    * Spin up an additional read-replica for the database


Finally, there are the communications mechanisms for the team. Many folks will
hear "weekly meeting" and wonder where the daily stand-up went. The more folks
in a meeting, the harder communication is. Instead of having regular
synchronization points, I prefer teams where individuals reach out to their
team mates regularly, many times through the day, to discuss shared work and
ask for help, using something like IRC or Slack. The issue tracker and code
review system are also points of collaboration which help team members keep up
to date on what others are working on. Teams should be no larger than 6-10
people, and as teams grow larger their areas of responsibility are split, often
by refactoring code into disparate services.

Elements of my ideal work environment are taken from many different places I've
worked. Underlying many of the idea here is an emphasis on regular
communication and collaboration between team members. Every patch that makes it
into production is a joint effort of many people, and reflects a dedication to
team work and a commitment to developing great software.

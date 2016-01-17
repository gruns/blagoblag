Don't have environments
=======================

    Almost every good idea this blog post comes from `David Reid`_, the bad
    ones are mostly mine*

Let's say you're making a website. Your customers (and randos who maybe you'd
like to be your customers) need to access it, so you create a **production**
environment at ``https://my-great-or-maybe-not-so-great-whatever-product.com``
and you tell people to go there.

Then you start working on the next great feature. It's basically done, but you
want to run it by some other folks and coordinate a launch plan for it, so you
merge it into ``master`` and create a ``production`` branch without it. Now all
your production deploys come from that branch, and people can freely land
stuff. And everything is great. You set up a **staging** environment, which
deploys from ``master``, so people can see what stuff looks like.

A few months pass, and the whole team is doing this workflow. Pull requests get
merged into ``master``, and then when you're ready to ship the whole thing you
merge ``master`` into ``production`` and deploy.

Then you have an emergency and need to deploy something to production
immediately, but you don't want to deploy all the other stuff on ``master``,
maybe you need to bump the version of a dependency for a security fix.

You land the patch on ``master`` like normal, and then go to cherry-pick it
over to ``production``. Crap, it doesn't apply cleanly. You forgot that on
``master`` you totally reorganized how dependencies were listed.

No matter, you'll just cherry-pick that patch over too. You do that, but tests
are failing, turns out you did that reorganization to enable you to bump a
dependency, which was included in the same patch, that dependency bump broke
backwards compatibility, all the tests are failing and the PR which fixes that
is somewhere else.

Fuck it, this is too much of a mess, let's just deploy ``master``, the staging
environment looks fine anyways. You do that, and stuff looks like it's ok,
except shit `Sentry`_ is going bananas which exceptions, it looks like you
totally broke one of the workflow. Damn, I remember leaving that review, "Let's
land this as is but make sure we fix this bug before the next deploy". I guess
we need to rollback and fix the issue, hopefully no one exploits the security
issue we were trying to fix in the first place.

Eventually you get it fixed and decide you need a new environment, so it's
easier to deploy critical fixes. Now you've got **production**, **staging**,
and **testing**.

If you do this long enough, you'll end up with:

* Development
* DevTest
* SQA (Software Quality Assurance)
* UAT (User Acceptance Testing)
* Demo
* PDT (Production Test)
* Field Test
* Prod Test (which is different from PDT)
* Performance
* Production

It's probably possible to come up with more environmnets, but this is more than
enough that I have no clue what any of these mean, or what the differences
between them are.

No matter how many environments you create, and force changes to flow through,
you can't escape the fact that if you merge things that aren't ready to be
deployed to **production** in one of these environements, the process of
flowing an unrelated patch through it will be harder and more ad-hoc. Pull
requests which are not ready should not be merged into the production track,
and ones which are only later discovered to not have been ready should be
reverted, and then reintroduced once they are fixed.

The way to address this problem is to not have a *fixed number* of
environments. Any fixed flow will encounter these same problems, instead you
want to focus on pull request review being the unit of "ok to deploy to
production".

How do you address the desire of people to see what not-yet-deployed work looks
like in this context? Instead of having a fixed number environments, have ∞
environments. Specifically, give every single pull request it's own
environment, and have the tooling to spin up and tear down any other
environments you want (e.g. for benchmarking) on demand.

In short, every project should have what Heroku calls `"Review Apps"`_. Every
pull request gets it's own deployed environment on demand, allowing it to be
demoed and reviewed. Pull requests are only merged into ``master`` when they
are ready to go to **production**, and they're reverted if they turn out to
have been unready.

When features are large, and require many separate pull requests to form the
full user-facing functionality, `feature flags`_ should be used, rather than
creating massive branches with everything in them.

In short, don't create fixed deployment pipelines composed of testing, and
staging, and pre-production environments. Instead maintain only *one* standing
environment, production. Manage everything else through short lived
per-pull-request deployments.

.. _`David Reid`: https://dreid.org/
.. _`Sentry`: https://getsentry.com/welcome/
.. _`"Review Apps"`: https://devcenter.heroku.com/articles/github-integration-review-apps
.. _`feature flags`: https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/

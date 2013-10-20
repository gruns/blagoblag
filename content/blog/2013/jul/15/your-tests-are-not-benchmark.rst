
Your tests are not a benchmark
==============================


I get a lot of feedback about people's experiences with PyPy. And a lot of it
is really great stuff for example, "We used to leave the simulation running
over night, now we take a coffee break". We also get some less successful
feedback, however quite a bit of that goes something like, "I ran our test
suite under PyPy, not only was it not faster, it was slower!". Unfortunately,
for the time being, this is really expected, we're working on improving it, but
for now I'd like to explain why that is.

* Test runs are short: Your test suite takes a few seconds, or a few minutes to
  run. Your program might run for hours, days, or even weeks. The JIT works by
  observing what code is run frequently and optimizing that, this takes a bit
  of time to get through the "observer phase", and during observation PyPy is
  really slow, once observation is done PyPy gets very very fast, but if your
  program exits too quickly, it'll never get there.
* Test code isn't like real code: Your test suite is designed to try to execute
  each pieces of code in your application exactly once. Your real application
  repeats the same task over and over and over again. The JIT doesn't kick in
  until a piece of code has been run over 1000 times, so if you run it just a
  small handful of times, it won't be fast.
* Test code really isn't like real code: Your test code probably does things
  like monkeypatch modules to mock things out. Monkeypatching a module will
  trigger a bit of deoptimization in PyPy. Your real code won't do this and so
  it will be fully optimized, but your test suite does hit the deoptimization
  and so it's slow.
* Test code spends time where app code doesn't: Things like the setup/teardown
  functions for your tests tend to be things that are *never* run in your
  production app, but sometimes they're huge bottlenecks for your tests.
* Test suites often have high variability in their runtimes: I don't have an
  explanation for why this is, but it's something observed over a large number
  of test suites. Bad statistics make for really bad benchmarks, which makes
  for bad decision making.

If you want to find out how fast PyPy (or any technology) is, sit down and
write some benchmarks, I've got `some advice on how to do that`_.

.. _`some advice on how to do that`: https://speakerdeck.com/alex/benchmarking

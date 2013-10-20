
A quick update
==============


I've now set up Al to be using GMP for all integers, and I'll be doing the same for floats once they get implemented.  I haven't started benchmarking yet, but it can compile and calculate the factorial of 50000 pretty quickly, and in Python vanilla that would result in a RuntimeError due to a stack overflow, so it's a good starting point.  Sorry for such a short post, I'm pretty tired today.

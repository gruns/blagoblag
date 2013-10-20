
Programming Languages Terminology
=================================


This semester I've been taking a course titled "Programming Languages".  Since I'm a big languages and compilers nerd this should be wonderful.  Unfortunately every time I'm in this class I'm reminded of just what a cluster-fuck programming language terminology is.  What follows are my definitions of a number of terms:

 * *Dynamic typing (vs static typing)*: Values do not have a type until runtime. Has nothing to do with the declaration of types (i.e. a type inferenced language is not dynamically typed).
 * *Type safety (vs type unsafety)*: Operations cannot be performed on values which do not support them, these operations need not be prohibited prior to execution, a run time exception suffices.
 * *Strong typing (vs weak typing)*: Implicit conversions are not performed. This has nothing to do with static or dynamic typing. Rather it references to whether a language will perform an operation such as ``'1' + 2``.  For example Python raises a ``TypeError`` here, whereas PHP returns ``3``. This one is slightly muddied by the fact that in languages with user defined types (and the ability to implement behaviors on operators), a type can really do anything it likes, thus this is less of an aspect of the core language and more one of the included types and functions.
 
There are probably some terms I've missed, but for these terms I think my definitions roughly match the consensus on them.

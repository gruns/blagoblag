
My Programming Language - Status Update
=======================================

:tags: al, c++, compile, python

Over the past few weeks I've been working on compiling my programming language.  At present it works by translating the source into C++, and then you compile that with your compiler of choice.  It's garbage collected, using the excellent Boehm GC library.  At present it can only compile a limited subset of what it can actually parse, or what the interpreter supports.  As of today thought it can compile and run a factorial function, however it can't calculate any factorial greater than 12, due to integer overflow issues.  To solve this I'm either going to use GMP or roll my own Bignum library, and I'm not sure which yet.  On the whole though, progress is good.  The generated C++ is about as good as it could be considering the limitations inherent in turning an interpreted language into a compiled one.  I haven't started benchmarking it yet, that was originally going to be the point of today's post before I ran into the integer overflow issues, however this is an example of the C++ code that is generated.

Give this Al(also valid Python):

.. sourcecode:: python
    
    def fact(n):
       if n == 1 or n == 0:
           return 1
       return n * fact(n-1)
    
    print(fact(1))
    print(fact(12))

It generated the following C++:

.. sourcecode:: c++
    
    #include "src/base.h"
    
    AlObj *fact;
    class f0:public AlFunction
    {
    public:
     virtual AlObj * operator () (ARG_TYPE args, KWARG_TYPE kwargs)
     {
       AlObj *n = args.back ();
         args.pop_back ();
       if (*
     ((*((*(n)) == (AlObj *) (new AlInt (1))))
      || (*(n)) == (AlObj *) (new AlInt (0))))
         {
     return (AlObj *) (new AlInt (1));;
         }
       ARG_TYPE t0;
       t0.push_back ((*(n)) - (AlObj *) (new AlInt (1)));
       return (*(n)) * (*fact) (t0, KWARG_TYPE ());
     }
    };
    
    int
    main ()
    {
     fact = new f0 ();
     ARG_TYPE t1;
     ARG_TYPE t2;
     t2.push_back ((AlObj *) (new AlInt (1)));
     t1.push_back ((*fact) (t2, KWARG_TYPE ()));
     (*print) (t1, KWARG_TYPE ());
     ARG_TYPE t3;
     ARG_TYPE t4;
     t4.push_back ((AlObj *) (new AlInt (12)));
     t3.push_back ((*fact) (t4, KWARG_TYPE ()));
     (*print) (t3, KWARG_TYPE ());
    }

All said and done, I'm pretty impressed!  You can get all the code `here <http://github.com/alex/alex-s-language/tree/master>`_, all the compilation work is in the code-generation branch.

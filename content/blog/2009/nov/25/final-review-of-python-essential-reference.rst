
Final Review of Python Essential Reference
==========================================


Disclosure: I received a free review copy of the book.

Today I finished reading the Python Essential Reference and I wanted to share my final thoughts on the book.  I'll start by saying I still agree with everything I wrote in my initial review, specifically that it's both a great resource as well as a good way to find out what you don't already know.  Reading the second half of the book there were a few things that really exemplified this for me.

The first instance of this is the chapter on concurrency.  I've done some concurrent programming with Python, but it's mostly been small scripts, a multiprocess and multithreaded web scraper for example, so I'm familiar with the basic APIs for threading and multiprocessing.  However, this chapter goes into the full details, really covering the stuff you need to know if you want to build bigger applications that leverage these techniques.  Things like shared data for processes or events and condition variables for threads and the kind of things that the book gives a good explanation of, as well as good examples of how to use them.

The other chapter that really stood out for me is the one on network programming and sockets.  This chapter describes everything from the low-level select module up through through the included socket servers.  The most valuable part is an example of how to build an asynchronous IO system.  This example is about 2 pages long and it's a brilliant example of how to use the modules, how to make an asynchronous API feel natural, and what the tradeoffs of asynchronous versus concurrency are.  In addition, in the wake of the "* in Unix" posts from a while ago I found the section on the socket module interesting as it's something I've never actually worked directly with.

The rest of the book is a handy reference, but for me these two chapters are the types of things that earns this a place on my bookshelf.  The way Python Essential Reference balances depth with conciseness is excellent, it shows you the big picture for everything and gives you super details on the things that are really important.  I just got my review copy of Dive into Python 3 today, so I look forward to giving a review of it in the coming days.

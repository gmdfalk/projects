#!/usr/bin/env python2


import time
from random import randint

def beer():
    # In Python 2, reversed might even be fastest because it's evaluated lazily. But then again
    # we could just use xrange.
    #for i in list(reversed(range(100)))
    #for i in xrange(100)[::-1]
    for i in range(99,0,-1):
        if i == 1:
            print """
    %s bottle of beer on the wall, %s bottle of beer,
    Take it down and pass it around, no more bottles of beer on the wall.\n
    No more bottles of beer on the wall, no more bottles of beer.
    Go to the store and buy some more, 99 bottles of beer on the wall.""" % (i, i)
        else:
            print """
    %s bottles of beer on the wall, %s bottles of beer.
    Take one down and pass it around, %s bottles of beer on the wall.""" % (i, i, i-1)

def bugs():
    max_lernt = True
    bugs = 2
    while max_lernt:
        new_bugs = randint(1,6)
        print """
        %s little bugs in the code, %s little bugs,
        Take them down and patch 'em around, %s little bugs in the code.
        """ % (bugs, bugs, bugs+new_bugs)
        bugs += new_bugs
        time.sleep(5)

bugs()

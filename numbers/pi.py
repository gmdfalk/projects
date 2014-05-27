#!/usr/bin/env python2

# Enter a number and have the program generate PI up to that many decimal places.
# Keep a limit to how far the program will go.

import math
import itertools
from decimal import *


def factorial(n):
    if n<1:
        return 1
    else:
        return n * factorial(n-1)

def chudnovsky(length=25, iters=20): #http://en.wikipedia.org/wiki/Chudnovsky_algorithm
    getcontext().prec = length
    pi = Decimal(0)
    c = 0
    while c < iters:
        pi += (Decimal(-1)**c)*(Decimal(factorial(6*c))/((factorial(c)**3)*(factorial(3*c)))* (13591409+545140134*c)/(640320**(3*c)))
        c += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    print pi, "(chudnovsky)"

def approx_pi(N):
    acc = 0
    for i in range(N):
        sign = (-1)**i
        n = (i + 1)*2 - 1
        acc += sign*(1.0/(n*3**i))
    print "%.30f (approx_pi)" % (math.sqrt(12) * acc)

def iter_pi(n):
    terms = ((-1)**i * (1.0 / ((2*i+1) * 3**i)) for i in itertools.count())
    print "%.30f (iter_pi)" % (math.sqrt(12) * sum(itertools.islice(terms, n)))

def pi_ac29(iterations=100, precision=30):
    from itertools import islice
    pi = 1
    iterables = (i for i in range(iterations*2) if i > 2 and i % 2)
    try:
        for i in range(iterations):
            # Possibility 1.
            #~ pi -= (1.0/iterables.next())
            #~ pi += (1.0/iterables.next())
            # Possibility 2.
            pi = pi - (1.0/iterables.next()) + (1.0/iterables.next())
            # Possibility 3.
            #~ sliced = tuple(islice(iterables, 2))
            #~ pi = pi - (1.0/sliced[0]) + (1.0/sliced[1])
    except (StopIteration, IndexError):
        print "{0:.{2}} (math.pi) \n{1:.{2}} (pi_ac29)".format(math.pi,
            pi*4, precision)

def pi_ac30(iterations=100, precision=30):
    from itertools import islice
    pi = exp = 1
    iterables = (i for i in range(iterations*2) if i > 2 and i % 2)
    try:
        for i in range(iterations):
            sliced = tuple(islice(iterables, 2))
            pi -= (1.0/(sliced[0]*(3**exp)))
            exp += 1
            pi += (1.0/(sliced[1]*(3**exp)))
            exp += 1
    # This try except block doesn't seem right, does it? FIXME
    #~ except (StopIteration, IndexError, OverflowError):
    except:
        result = math.sqrt(12)*pi
        #~ print "%.30f versus %.30f" % (math.pi, result)
        print "{0:.{2}} \n{1:.{2}} (pi_ac30)".format(math.pi,
            result, precision)
        return result
    return math.sqrt(12)*pi

print "%.30f (math.pi)" % math.pi
chudnovsky(30, 50)
print "%.30f" % math.pi
approx_pi(400)
print "%.30f" % math.pi
iter_pi(600)
pi_ac29(200000)
pi_ac30(20000)

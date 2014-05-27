#! /usr/bin/env python2

import random
import math
import itertools

def rands():
    for i in range(10):
        print random.randint(0, 100), random.randrange(25,35)

def hypot(x, y):
    return math.sqrt(x**2+y**2)
    
hypo = lambda x, y: math.sqrt(x**2+y**2)

print hypot(-2, -2)
#~ print hypo(-1, -2)
print math.hypot(-2, -2)

def approx_pi(N):
  acc = 0
  for i in range(N):    # i    will be 0,  1,  2,  3, ..., N-1
    sign = (-1)**i      # sign will be 1, -1,  1, -1, ...
    n = (i + 1)*2 - 1   # n    will be 1,  3,  5,  7, ...
    acc += sign*(1.0/(n*3**i))
  return math.sqrt(12) * acc

def iter_pi(n):
  terms = ((-1)**i * (1.0 / ((2*i+1) * 3**i)) for i in itertools.count())
  return math.sqrt(12) * sum(itertools.islice(terms, n))

print math.pi
#~ print approx_pi(30)
print iter_pi(30)


#!/usr/bin/env python2

# Have the program find prime numbers until the user chooses to stop asking for
# the next one.

def isprime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def imperative():
    primes = (i for i in range(1000) if isprime(i))

    for p in primes:
        print p
        raw_input("next?")

###############################
# Simulating Haskell's "take" #
###############################
from itertools import islice

def integers():
    i = 1
    while True:
        yield i
        i += 1

def primes():
    for i in integers():
        if 1 < i < 4 or i % 2 and i % 3 and i != 1:
            yield i

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def functional(prime=1):
    while True:
        print take(prime, primes())[-1]
        prime += 1
        raw_input("next?")

# Both ways are a little convoluted, but hey, the more you try, the more you learn ;)
print take(100, primes())
#~ imperative()
functional()

#!/usr/bin/env python2

# Enter a number and have the program generate the Fibonacci sequence to that
# number or to the Nth number.

def fib(n):
    a = 0
    b = 1
    while a < n:
        print a,
        a, b = b, a+b

fib(1000)

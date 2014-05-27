#!/usr/bin/env python2

# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number and for the
# multiples of five print "Buzz". For numbers which are multiples of both three
# and five print "FizzBuzz".

for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0:
        msg = "FizzBuzz"
    elif i % 5 == 0:
        msg = "Buzz"
    elif i % 3 == 0:
        msg = "Fizz"
    else:
        msg = i
    print msg

#!/usr/bin/env python2

"Interactive Python Part 1: Quick Exercises"

import unittest

def alarm():
    """Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm,
    0 is midnight). If it is currently 13 and you set your alarm to go off in 50
    hours, it will be 15 (3pm). Write a Python program to solve the general
    version of the above problem. Ask the user for the time now (in hours), and
    then ask for the number of hours to wait for the alarm. Your program should
    output what the time will be on the clock when the alarm goes off."""
    
    hour_now = int(raw_input("what hour is it now? "))
    hours_to_wait = int(raw_input("how many hours to wait? "))
    hour_future = (hour_now + hours_to_wait) % 24
    print "after waiting", hours_to_wait, "hours, it'll be", hour_future, "o'clock"

def days():
    """It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6
    is Saturday. If you go on a wonderful holiday leaving on day number 3
    (a Wednesday) and you return home after 10 nights. Write a general version
    of the program which asks for the starting day number, and the length of your
    stay, and it will tell you the number of day of the week you will return on."""
    
    start_day = int(raw_input("from 0-6 what day is it? "))
    days_to_wait = int(raw_input("how many days are you gone? "))
    end_day = (start_day + days_to_wait) % 7
    print end_day

def jack_is_dull():
    """Take the sentence: All work and no play makes Jack a dull boy.
    Store each word in a separate variable, then print out the sentence on one
    line using print."""
    
    for i in ["All", "work", "and", "no", "play", "makes", "Jack", "a", "dull", "boy."]:
        print i,
    print
    
def compound_interest():
    """Write a Python program that assigns the principal amount of 10000 to
    variable P, assign to n the value 12, and assign to r the interest rate of
    8% (0.08). Then have the program prompt the user for the number of years, t,
    that the money will be compounded for. Calculate and print the final amount
    after t years.
    
    A = P(1+r/n)**nt
    """
    P = 10000
    r = 0.08
    n = 12
    t = int(raw_input("Number of years? "))

    result = P*(1+(r/n))**(n*t)

    print "For P = %s, r = %s and n = %s, the compound interest after %s years is:\n%.2f"\
        % (P, r, n, t, result)

def area_circle(radius):
    "Write a program that will compute the area of a circle."
    from math import pi
    return pi * radius**2

def area_rectangle(width, height):
    "Write a program that will compute the area of a rectangle."
    return width*height

def mpg(miles, gallons):
    """Write a program that will compute MPG for a car. Prompt the user to enter
    the number of miles driven and the number of gallons used. Print a nice
    message with the answer."""
    miles = float(miles) / gallons
    km = miles * 0.425
    print miles, "mpg or in km/liter:", km
    return miles

def celsius_to_fahrenheit(celsius):
    "Write a program that will convert degrees celsius to degrees fahrenheit."
    return ((celsius*9)/5.0)+32

def fahrenheit_to_celsius(fahrenheit):
    "Write a program that will convert degrees fahrenheit to degrees celsius."
    return ((fahrenheit-32)*5)/9.0

if __name__ == "__main__":
    #~ jack_is_dull()
    #~ compound_interest()
    assert area_rectangle(10, 15) == 150
    assert mpg(150, 12) == 12.5
    assert celsius_to_fahrenheit(94.5) == 202.1
    assert fahrenheit_to_celsius(202.1) == 94.5



class LazyTest(unittest.TestCase):

    def _test(self, func, *args, **kwargs):
        result = func(*args)
        self.assertEqual(result, kwargs['expected'])
        
    def test_circle(self):
        self._test(area_circle, 17.34, expected=944.6002560737031)
        
    def test_conversion(self):
        self._test(mpg, 69.6, 12.5, expected=5.568)

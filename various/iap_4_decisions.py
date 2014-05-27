#! /usr/bin/env python2

"Interactive Python Part 4: Decisions"

def graph_ac17(n=10):
    """Modify the turtle bar chart program from the previous chapter so that the
    bar for any value of 200 or more is filled with red, values between
    [100 and 200) are filled yellow, and bars representing values less than 100
    are filled green."""
    
    import turtle
    from random import randint
    
    wn = turtle.Screen()
    wn.delay(0.1)
    t = turtle.Turtle()
    t.color("blue")
    t.left(90)
    for i in range(n):
        x = randint(-100,250)
        if x >= 200:
            t.fillcolor("red")
        elif 100 <= x < 200:
            t.fillcolor("yellow")
        elif 0 <= x < 100:
            t.fillcolor("green")
        else:
            t.fillcolor("orange")
        t.begin_fill()
        if x <= 0: t.write(x)
        t.forward(x)
        t.right(90)
        if x > 0: t.write(x)
        t.forward(20)
        t.left(90)
        t.forward(-x)
        t.end_fill()
    t.color("blue")
    t.left(90)
    t.forward(n*20)
    wn.exitonclick()

def hypot_ac19(a, b):
    """Write a function findHypot. The function will be given the length of two
    sides of a right-angled triangle and it should return the length of the
    hypotenuse. (Hint: x ** 0.5 will return the square root, or use sqrt from
    the math module)"""
    
    import math
    #~ return math.hypot(a, b)
    return (a**2 + b**2)**0.5
    #~ return math.sqrt(a**2 + b**2)

def iseven(n):
    "Write a function called is_even(n) that takes an integer as an argument\
    and returns True if the argument is an even number and False if it is odd."
    return n % 2 == 0

def isodd(n):
    """Now write the function is_odd(n) that returns True when n is odd and False otherwise.
    ...
    Modify is_odd so that it uses a call to is_even to determine if its argument is an odd integer."""
    
    return not iseven(n)

def is_rightangled_ac23(a, b, c):
    """Write a function is_rightangled which, given the length of three sides of
    a triangle, will determine whether the triangle is right-angled. Assume that
    the third argument to the function is always the longest side. It will return
    True if the triangle is right-angled, or False otherwise.
    Extend the (above) program so that the sides can be given to the function in
    any order."""
    # Sorting the list to pin down the biggest number.
    L = sorted([a,b,c])
    # Another way would be to rest = L.remove(max(L))
    # Plus big = set(L) & set(rest) (or {L} & {rest} if using tuples and nex
    # set literal syntax in py2.7 or py3.
    # Keeping the order: [i for i, j in zip(L, rest) if i == j]
    # Or inverted: big = max([a,b,c]) and rest = L.remove(big)
    epsilon = 0.001
    result = L[0]**2 + L[1]**2
    if abs(L[2]**2-result) < epsilon:
        return True
    else:
        return False

def leap_ac25(year):
    """A year is a leap year if it is divisible by 4 unless it is a century that
    is not divisible by 400. Write a function that takes a year as a parameter
    and returns True if the year is a leap year, False otherwise."""
    year = float(year)
    if year % 4 == 0:
        if year % 400 != 0 and year % 100 == 0:
            return False
        else:
            return True

def easterdate_ac26(year):
    """Implement the calculator for the date of Easter.
    The following algorithm computes the date for Easter Sunday for any year
    between 1900 to 2099. Ask the user to enter a year. Compute the following:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        dateofeaster = 22 + d + e
    """

    assert 1900 <= year <= 2099
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    result = 22 + d + e
    if year in (1954, 1981, 2049, 2076):
        result -= 7
    
    if result > 31:
        print "April", result-31
        return result-31
    else:
        print "March", result
        return result

if __name__ == "__main__":
    #~ print grade_ac16(80.999)
    #~ graph_ac17()
    print hypot_ac19(12, 3)
    assert iseven(44) == True
    assert iseven(7) == False
    assert isodd(371) == True
    assert isodd(92) == False

    assert is_rightangled_ac23(3.0, 4.0, 5.0) == True

    assert leap_ac25(1800) == False
    assert leap_ac25(2000) == True
    assert leap_ac25(2016) == True
    assert leap_ac25(2500) == False

    assert easterdate_ac26(2014) == 20

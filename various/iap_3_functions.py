#! /usr/bin/env python2

"Interactive Python Part 3: Functions"

import turtle
import math
from random import randint

def polygon(length, sides):
    angle = 360 / sides
    for i in range(sides):
        t.left(angle)
        t.forward(length)

def circle(radius):
    circumference = 2 * 3.1415 * radius
    length = circumference / 360
    polygon(length, 360)

def graph_ac14(n=10):
    t.left(90)
    for i in range(n):
        x = randint(50,150)
        if i % 2:
            t.color("red")
        else:
            t.color("purple")
        t.begin_fill()
        t.forward(x)
        t.right(90)
        t.write(x)
        t.forward(20)
        t.left(90)
        t.forward(-x)
        t.end_fill()

def five_squares_ac15(length=20):
    """Use the drawsquare function we wrote in this chapter in a program to draw
    the image shown below. Assume each side is 20 units. (Hint: notice that the
    turtle has already moved away from the ending point of the last square when
    the program ends.)"""
    for i in range(5):
        polygon(length, 4)
        t.penup()
        t.forward(length*2)
        t.pendown()

def growing_squares_ac16(length=20):
    """Write a program to draw this. Assume the innermost square is 20 units
    per side, and each successive square is 20 units bigger, per side, than
    the one inside it."""
    t.color("red")
    for i in range(6):
        polygon(length, 4)
        t.penup()
        t.right(45)
        t.forward(14)
        t.left(45)
        t.pendown()
        length += 20

def labyrinth_ac19(length=1, angle=90):
    "The two spirals in this picture differ only by the turn angle. Draw both."
    for i in range(95):
        t.right(angle)
        t.forward(length)
        length += 2
        #~ angle += 0.01
    t.right(90)

def sum_ac21(n):
    """Write a fruitful function sumTo(n) that returns the sum of all integer
    numbers up to and including n. So sumTo(10) would be 1+2+3...+10 which would
    return the value 55. Use the equation (n * (n + 1)) / 2."""
    #~ return sum(i for i in range(1, n+1))
    return (n*(n+1))*0.5

def star_ac23(n=5):
    "Write a non-fruitful function to draw a five pointed star, where the length\
    of each side is 100 units."
    assert n > 2 and n % 2 != 0, "input must be an odd integer greater than 2"
    for i in range(n):
        t.forward(100)
        t.right(180-180.0/n)

def stars_ac24():
    """Extend your program above. Draw five stars, but between each, pick up the
    pen, move forward by 350 units, turn right by 144, put the pen down, and draw
    the next star. You’ll get something like this (note that you will need to
    move to the left before drawing your first star in order to fit everything
    in the window):"""
    
    t.color("red")
    t.penup()
    t.forward(-150)
    t.pendown()
    for i in range(5):
        star_ac23()
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()

def sqrt_ac28(n):
    """Write a function called mySqrt that will approximate the square root of a
    number, call it n, by using Newton’s algorithm. Newton’s approach is an
    iterative guessing algorithm where the initial guess is n/2 and each
    subsequent guess is computed using the formula:
    newguess = (1/2) * (oldguess + (n/oldguess))."""
    
    oldguess = n * 0.5
    for i in range(500):
        newguess = 0.5 * (oldguess + (n/oldguess))
        # To avoid unnecessary repetition:
        if newguess == oldguess: return newguess
        oldguess = newguess
        print oldguess, newguess
    return newguess

def pi_ac29(iterations=100):
    "Write a function called myPi that will return an approximation of PI\
    (3.14159...). Use the Leibniz approximation."
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
        print math.pi, "versus",
        return pi*4
    return pi*4

def pi_ac30(iterations=100, precision=25):
    "Write a function called myPi that will return an approximation of PI\
     (3.14159...). Use the Madhava approximation."
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
        print "{0:.{2}} (math.pi) \n{1:.{2}} (your result)".format(math.pi,
            result, precision)
        return result
    return math.sqrt(12)*pi

def sprite(legs=14, length=50):
    """Write a function called drawSprite that will draw a sprite. The function
    will need parameters for the turtle, the number of legs, and the length of
    the legs. Invoke the function to create a sprite with 15 legs of length 120."""
    t.color("black")
    for i in range(legs):
        t.forward(length)
        t.forward(-length)
        t.right(360.0/legs)

def fancysquare_ac31():
    """Write a function called fancySquare that will draw a square with fancy
    corners (spites on the corners). You should implement and use the drawSprite
    function from above. For an even more interesting look, how about adding
    small triangles to the ends of the sprite legs."""
    
    t.color("red")
    for i in range(4):
        t.forward(200)
        sprite()
        t.color("red")
        t.right(90)

wn = turtle.Screen()
wn.delay(0.001)
t = turtle.Turtle()
t.color("blue")

#~ graph_ac14()
#~ five_squares_ac15()
#~ growing_squares_ac16()
#~ labyrinth_ac19()
#~ print sum_ac21(10)
#~ star_ac23() 
#~ stars_ac24()
#~ print sqrt_ac28(512)
#~ print pi_ac29(100000)
print pi_ac30(300)
#~ fancysquare_ac31()

wn.exitonclick()

#!/usr/bin/env python2

"Interactive Python Part 2: Turtles!"

import turtle
from time import sleep

wn = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("red")

def polygon(sides=4, length=100, color="green"):
    t.color(color)
    t.begin_fill()
    for i in range(sides):
        t.forward(length)
        t.left(360.0/sides)
    t.end_fill()

def drunk():
    """A drunk pirate makes a random turn and then takes 100 steps forward, makes
    another random turn, takes another 100 steps, turns another random amount,
    etc. A social science student records the angle of each turn before the next
    100 steps are taken. Her experimental data is 160, -43, 270, -97, -43, 200,
    -940, 17, -86. (Positive angles are counter-clockwise.) Use a turtle to draw
    the path taken by our drunk friend. After the pirate is done walking, print
    the current heading."""
    
    t.color("purple")
    t.pendown()
    for turn in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
        t.left(turn)
        t.forward(100)
    print t.position()

def star(size=11, inverted=0, angle=144):
    "Write a program to draw a star"
    t.color("red")
    t.penup()
    t.forward(-350)
    t.pendown()
    if inverted:
        angle = 216
    for i in range(5):
        t.forward(size*12)
        t.right(angle)
        
    if inverted:
        t.right(-103)
        for i in range(40):
            t.forward(size)
            t.right(9)
        t.penup()
        t.right(100)
        t.forward(size*6)
        t.left(90)
        t.forward(size*1.5)
        t.left(180)
        print "Hail Baphomet"
    else:
        t.penup()
        t.forward(size*6)
        t.right(90)
        t.forward(size*2)
        t.right(180)
    for i in ["yellow", "green", "red", "yellow", "green", "red"]:
        t.color(i)
        sleep(0.5)

def clock(size=100):
    "Write a program to draw a face of a clock that looks something like this:\
    http://interactivepython.org/courselib/static/thinkcspy/_images/tess_clock1.png"
    t.color("blue")
    fullsize=-(size+3*(size/10.0))
    for i in range(12):
        t.penup()
        t.forward(size)
        t.pendown()
        t.forward(size/10.0)
        t.penup()
        t.forward(2*(size/10.0))
        t.stamp()
        t.forward(fullsize)
        t.right(30)

def tanenbaum():
    tanenbaum = turtle.Turtle()

    tanenbaum.hideturtle()
    tanenbaum.speed(40)

    for i in range(350):
        tanenbaum.forward(i)
        tanenbaum.right(98)

def sprite(legs=96):
    """A sprite is a simple spider shaped thing with n legs coming out from a
    center point. The angle between each leg is 360/n degrees.
    Write a program to draw a sprite where the number of legs is provided by
    the user."""
    
    t.pendown()
    wn.delay(0.0001)
    t.color("black")
    for i in range(legs):
        t.forward(100)
        t.forward(-100)
        t.right(360.0/legs)

def sprite_org(legs=96):
    wn.delay(0.0001)
    t.shape("circle")
    t.color("red")

    angle = 360.0/legs

    for i in range(legs):
        # draw the leg
        t.right(angle)
        t.forward(120)
        t.stamp()

        # go back to the middle and turn back around
        t.right(180)
        t.forward(120)
        t.right(180)

# Triangle
polygon(3)
# Square
polygon(4)
# Hexagon
polygon(6)
# Octagon
polygon(8)
drunk()
star(20, 1)
clock()
tanenbaum()
sprite()
sprite_org()

wn.exitonclick()

##############
# Old Turtle #
##############

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, degree, corners):
    for i in range(corners):
        fd(t, length)
        lt(t, degree)

def circle(t, radius):
    polygon(t, radius, 10, 36)

def arc(t, radius, degrees):
    corners = degrees/10
    length = 10
    polygon(t, radius, length, corners)

square(bob, 50)
polygon(bob, 50, 60, 8)
circle(bob, 20)
arc(bob, 10, 180)
wait_for_user()

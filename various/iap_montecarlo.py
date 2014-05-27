#! /usr/bin/env python2

# Approximate pi via a Monte Carlo Simulation:
# http://interactivepython.org/courselib/static/thinkcspy/Labs/montepi.html
# 100k darts = 3.13988 4min, tracer 1000
# 10k darts = 3.1423, 13.4s, tracer 100

import turtle
import math
import random

t = turtle.Turtle()
t.up()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)
wn.delay(0.1)
t.tracer(100)

darts = 10000
hits = 0
t.up()
for i in range(darts):
    randx = random.random()
    randy = random.random()

    x = 2*(randx-0.5)
    y = 2*(randy-0.5)

    t.setpos(x,y)
    if t.distance(0,0) < 1:
        hits += 1.0
        t.color("red")
        t.dot()
    else:
        t.color("blue")
        t.dot()
    #~ print i,

print (hits/darts)*4

wn.exitonclick()

#!/usr/bin/env python2
# *-* coding: utf-8 *-*

"Interactive Python Part 11: OOP"

from __future__ import division
import turtle
from math import sqrt

class Point(object):
    " Point class for representing and manipulation cartesian coordinates"
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return str(self.x)+","+str(self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)
        
    def distance_to_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance_to(self, point):
        """Add a distanceFromPoint method that works similar to
        distanceFromOrigin except that it takes a Point as a parameter and
        computes the distance between that point and self."""
        dx = point.get_x()-self.x
        dy = point.get_y()-self.y

        return sqrt(dx**2 + dy**2)

    def reflect(self):
        """Add a method reflect_x to Point which returns a new Point, one which
        is the reflection of the point about the x-axis. For example,
        Point(3, 5).reflect_x() is (3, -5)"""
        return self.x, -self.y

    def slope_to_origin(self):
        """Add a method slope_from_origin which returns the slope of the line
        joining the origin to the point."""
        if self.x:
            return self.y/self.x

    def move(self, units):
        """Add a method called move that will take two parameters, call them dx
        and dy. The method will cause the point to move in the x and y direction
        the number of units given."""
        self.x += units
        self.y += units


def center_circle(p1, p2, p3):
    """Given three points that fall on the circumference of a circle, find the
    center and radius of the circle."""
    mr = (p2.y - p1.y) / (p2.x - p1.x)
    mt = (p3.y - p2.y) / (p3.x - p2.x)
    x = (mr*mt*(p3.y-p1.y)+mr*(p2.x+p3.x)-mt*(p1.x+p2.x))/(2*(mr-mt))
    y = -(1/mr)*(x-((p1.x+p2.x)/2))+(p1.y+p2.y)/2
    center = (x, y)
    radius = sqrt((p2.x-x)**2+(p2.y-y)**2)
    print "center is: ", center
    print "radius is: ", radius
    

class Fraction(object):

    def __init__(self, top, bottom):
        self.num = top        #the numerator is on top
        self.den = bottom     #the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def gcd(self, m, n):
        "Greatest Common Denominator"
        while m % n:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn

        return n

    def simplify(self):
        common = self.gcd(self.num, self.den)

        self.num /= common
        self.den /= common


    def __add__(self, fract):
        newnum = self.num * fract.den + self.den * fract.num
        newden = self.den * fract.den

        common = self.gcd(newnum, newden)

        return Fraction(newnum / common, newden / common)

    def __mul__(self, fract):
        newnum = self.num * fract.num
        newden = self.den * fract.den

        return Fraction(newnum, newden)
        
    __rmul__ = __mul__


class Rectangle(object):

    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

    def __str__(self):
        return "%s %s" % (str(self.width), str(self.height))

    def get_width(self):
        return self.width
        
    def get_height(self):
        return self.height

    def area(self):
        """Add a method area to the Rectangle class that returns the area of
        any instance"""
        return self.width * self.height

    def perimeter(self):
        """Write a perimeter method in the Rectangle class so that we can find
        the perimeter of any rectangle instance"""
        return 2 * (self.width + self.height)

    def transpose(self):
        """Write a transpose method in the Rectangle class that swaps the width
        and the height of any rectangle instance"""
        self.width, self.height = self.height, self.width

    def diagonal(self):
        """Write a new method called diagonal that will return the length of the
        diagonal that runs from the lower left corner to the opposite corner."""
        return sqrt(self.width**2 + self.height**2)

    def contains(self, point):
        """Write a new method in the Rectangle class to test if a Point falls
        within the rectangle. For this exercise, assume that a rectangle at (0,0)
        with width 10 and height 5 has open upper bounds on the width and height,
        i.e. it stretches in the x direction from [0 to 10), where 0 is included
        but 10 is excluded, and from [0 to 5) in the y direction. So it does not
        contain the point (10, 2)."""
        x, y = point.get_x(), point.get_y()
        return 0 <= x < self.width and 0 <= y < self.height

    def collides_with(self):
        """In games, we often put a rectangular “bounding box” around our sprites
        in the game. We can then do collision detection between, say, bombs and
        spaceships, by comparing whether their rectangles overlap anywhere.
        Write a function to determine whether two rectangles collide. Hint: this
        might be quite a tough exercise! Think carefully about all the cases
        before you code."""
        # TODO
        pass

        
if __name__ == "__main__":
    # Points
    p = Point(5, 5)
    q = Point(6, -2)
    r = Point(2, -4)
    center_circle(p,q,r)
    
    # Fractions
    myfraction = Fraction(12, 16)
    print myfraction.get_num()
    print myfraction.get_den()
    print myfraction.gcd(4, 98)
    myfraction.simplify()
    f1 = Fraction(1,2)
    f2 = Fraction(1,4)
    f4 = f1 * f2

    # Rectangle
    R = Rectangle(Point(4,5), 10, 5)
    assert R.area() == 50
    assert R.perimeter() == 30
    R.transpose()
    print R.diagonal()

    r = Rectangle(Point(0, 0), 10, 5)
    assert r.contains(Point(0, 0)) == True
    assert r.contains(Point(3, 3)) == True
    assert r.contains(Point(3, 7)) == False
    assert r.contains(Point(3, 5)) == False
    assert r.contains(Point(3, 4.99999)) == True
    assert r.contains(Point(-3, -3)) == False
   

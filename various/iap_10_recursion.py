#!/usr/bin/env python2
# *-* coding: utf-8 *-*

"""Interactive Python Part 10: Recursion:

    A recursive algorithm must have a base case.
    A recursive algorithm must change its state and move toward the base case.
    A recursive algorithm must call itself, recursively."""


def sumiter(lst):
    result = 0
    for i in lst:
        result += i
    return result

def sumrecurse(lst):
    "Write a recursive function to compute the sum of a list."
    if len(lst) <= 1:
        return lst[0]
    return lst[0] + sumrecurse(lst[1:])

def factorialiter(n):
    product = 1
    for i in range(n):
        product *= (i+1)
    return product

def factorialrecurse(n):
    "Write a recursive function to compute the factorial of a number."
    if n <= 1:
        return n
    return n * factorialrecurse(n-1)

def baseconvert(n, base=16):
    from string import uppercase
    
    if not 1 < base < 37: return
    
    if base <= 10:
        basecases = ''.join(str(i) for i in range(base))
    else:
        first10 = ''.join(str(i) for i in range(10))
        next26 = uppercase[:base-10]
        basecases = first10 + next26

    if n < base:
        return basecases[n]
    return baseconvert(n // base, base) + basecases[n % base]

def reverse(s):
    """Write a function that takes a string as a parameter and returns a new
    string that is the reverse of the old string."""
    if len(s) == 1:
        return s
    return reverse(s[1:]) + s[0]

def palindrome(s):
    """Write a function that takes a string as a parameter and returns True if
    the string is a palindrome, False otherwise. Remember that a string is a
    palindrome if it is spelled the same both forward and backward. For example:
    "radar" is a palindrome. for bonus points palindromes can also be phrases, but
    you need to remove the spaces and punctuation before checking. For example:
    "madam i’m adam" is a palindrome."""
    from string import letters
    if len(s) <= 1:
        return True
    s = ''.join([i.lower() for i in s if i in letters])
    return s[0] == s[-1] and palindrome(s[1:-1])

def turtletree():
    import turtle
    from random import randrange

    def tree(branchLen,t, width=5, color="brown"):
        if branchLen > 5:
            t.width(width)
            t.color(color)
            t.forward(branchLen)
            t.right(20)
            tree(branchLen-15, t, width-1, "green")
            t.left(50)
            tree(branchLen-15, t, width-1)
            t.right(30)
            t.backward(branchLen)
            
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    tree(75,t)
    myWin.exitonclick()

def turtlesierpinski():
    import turtle

    def drawTriangle(points,color,myTurtle):
        myTurtle.fillcolor(color)
        myTurtle.up()
        myTurtle.goto(points[0][0],points[0][1])
        myTurtle.down()
        myTurtle.begin_fill()
        myTurtle.goto(points[1][0],points[1][1])
        myTurtle.goto(points[2][0],points[2][1])
        myTurtle.goto(points[0][0],points[0][1])
        myTurtle.end_fill()

    def getMid(p1,p2):
        return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

    def sierpinski(points,degree,myTurtle):
        colormap = ['blue','red','green','white','yellow',
                    'violet','orange']
        drawTriangle(points,colormap[degree],myTurtle)
        if degree > 0:
            sierpinski([points[0],
                            getMid(points[0], points[1]),
                            getMid(points[0], points[2])],
                       degree-1, myTurtle)
            sierpinski([points[1],
                            getMid(points[0], points[1]),
                            getMid(points[1], points[2])],
                       degree-1, myTurtle)
            sierpinski([points[2],
                            getMid(points[2], points[1]),
                            getMid(points[0], points[2])],
                       degree-1, myTurtle)

    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-100,-50],[0,100],[100,-50]]
    sierpinski(myPoints,3,myTurtle)
    myWin.exitonclick()

def reverselist(lst):
    "Write a recursive function to reverse a list"
    if not len(lst):
        return lst
    return  reverselist(lst[1:]) + [lst[0]]

def fibrecur(n):
    """Write a recursive function to compute the Fibonacci sequence. How does the
    performance of the recursive function compare to that of an iterative version?"""
    if n <= 1: return n
    return fibrecur(n-1) + fibrecur(n-2)

def fibiter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    print a

def test(func, iterations=1):
    """Unique values, defeats memo-ization."""
    for x in range(iterations):
        func(30)

def timethese(n=1):
    import timeit
    
    setup = 'from __main__ import test, fibrecur, fibiter'
    
    t1 = timeit.repeat('test(fibrecur)', setup, number=n)
    t2 = timeit.repeat('test(fibiter)', setup, number=n)
    print 'recursive', t1
    print 'iterative', t2
    print 'Difference', min(t1) / min(t2)

def turtlekoch():
    import turtle

    def koch(aturtle, length):
        if length <= 5:
            aturtle.forward(length)
        else:
            koch(aturtle,length/3)
            aturtle.left(60)
            koch(aturtle,length/3)
            aturtle.right(120)
            koch(aturtle,length/3)
            aturtle.left(60)
            koch(aturtle,length/3)


    t = turtle.Turtle()
    wn = turtle.Screen()

    t.up()
    t.backward(200)
    t.down()
    wn.setworldcoordinates(0,0,330,100)
    t.speed(50)

    koch(t, 400)
    wn.exitonclick()
    
if __name__ == "__main__":
    assert sumiter([1,2,3,4]) == 10
    assert sumrecurse([1,2,3,4,5]) == 15
    assert factorialiter(5) == 120
    assert factorialrecurse(5) == 120
    assert baseconvert(17910, 16) == "45F6"
    assert baseconvert(100, 2) == "1100100"
    assert baseconvert(100, 8) == "144"
    assert baseconvert(100, 10) == "100"
    assert baseconvert(100, 16) == "64"
    assert reverse("pirate") == "etarip"
    assert palindrome("A man, a plan, a canal: Panama!") == True
    assert palindrome("This is not a palindrome.") == False
    assert reverselist(["a",[1],0,4]) == [4,0,[1],"a"]
    #~ fibiter(35)
    #~ fibrecur(35)
    #~ timethese(10)
    #~ turtletree()
    #~ turtlesierpinski()
    turtlekoch()
    

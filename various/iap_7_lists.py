#!/usr/bin/env python2

"Interactive Python Part 7: Lists"

from random import randrange

def isprime(n):
    "Write a function that checks if a number is a prime"
    if n < 2: return False
    for i in 2, 3:
        if n % i == 0 and i != n:
            return False
    return True

def getprimes(n):
    "Write a function that returns all prime numbers up to n"
    return [i for i in range(n) if isprime(i)]

def getprimes_silly(n):
    "Doing it the Perl way."
    print(list(filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0,
    map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(2,n+1)))))

def getprimes_sieve(n):
    primes = dict.fromkeys(range(3,n+1,2),True)
    sieve_list = [2]
    for num in sorted(primes):
        if primes[num] == True:
            sieve_list.append(num)
            j = num ** 2
            while j < n:
                if j in primes:
                    primes[j] = False
                j += num
    return(sieve_list)

def average(data):
    """Create a list containing 100 random integers between 0 and 1000 (use
    iteration, append, and the random module). Write a function called average
    that will take the list as a parameter and return the average."""
    return sum(data)/len(data)

def maximum(data):
    """Write a Python function that will take a list of 100 random integers
    between 0 and 1000 and return the n value. (Note: there is a builtin
    function named max but pretend you cannot use it.)"""
    print [i for i in range(1000) if i in data][-1]
    print sorted(data)[-1]
    print max(data)
    last_seen = 0
    for i in data:
        if i > last_seen:
            last_seen = i
    print last_seen
    # Probably lots more ways but i'll stop here.

def squaresum(data):
    """Write a function sum_of_squares(xs) that computes the sum of the squares
    of the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should
    return 4+9+16 which is 29."""
    return sum(i**2 for i in data)

def countodd(data):
    "Write a function to count how many odd numbers are in a list."
    return sum(1 for i in data if i % 2)

def sumeven(data):
    "Sum up all the even numbers in a list."
    return sum(i for i in data if i % 2 == 0)

def sumnegative(data):
    "Sum up all the negative numbers in a list."
    return sum(i for i in data if i < 0)

def countlength(data):
    "Count how many words in a list have length 5."
    return sum(1 for i in data if len(i) == 5)

def sumexclude(data):
    "Sum all the elements in a list up to but not including the first even number."
    count = 0
    for i in data:
        if i % 2 == 0:
            break
        count += i
    return count

def countinclude(data, s="sam"):
    """Count how many words occur in a list up to and including the first
    occurrence of the word "sam"."""
    count = 0
    for i in data:
        count += 1
        if i == s:
            break
    return count

def list_methods():
    """Although Python provides us with many list methods, it is good practice
    and very instructive to think about how they are implemented.
    Implement a Python function that works like the following:

    count, in, reverse, index, insert
    """
    def count(data, s):
        count = 0
        for i in data:
            if i == s:
                count += 1
        return count

    def isin(data, s):
        for i in data:
            if i == s:
                return True
        return False
        
    def reverse(data):
        rev_list = []
        for i in data:
            rev_list.insert(0, i)
        return rev_list

    def index(data, s):
        for i in range(len(data)):
            if data[i] == s:
                return i

    def insert(data, n, s):
        # FIXME: Does not work if n > len(data).
        new_lst = []
        for i in range(len(data)):
            if i == n:
                new_lst.append(s)
            new_lst.append(data[i])
        return new_lst
        
    assert count([1, 2, 3, 3, 3, 3, 5], 3) == 4
    assert reverse([1, 2, 3]) == [3, 2, 1]
    assert index([1, 2, 3, 3, 3, 3, 5], 3) == 2
    assert isin(["as", 2, 91, "ffff"], "as") == True
    assert insert([1, 2, 3], 2, "a") == [1, 2, "a", 3]

def replace(s, old, new):
    return new.join(s.split(old))

def turtle_lsys(func="fib"):
    import turtle
        
    def apply_fib(char):
        newstr = ""
        if char == "F":
            newstr = "F-F++F-F"
        else:
            newstr = char
            
        return newstr
        
    def apply_branch(char):
        newstr = ""
        if char == "F":
            newstr = "F[-F]F[+F]F"
        else:
            newstr = char
            
        return newstr
        
    def apply_herb(char):
        newstr = ""
        if char == "H":
            newstr = "HFX[+H][-H]"
        elif char == "X":
            newstr = "X[-FFF][+FFF]FX"
        else:
            newstr = char
            
        return newstr

    def create_rules(axiom, iters=4, func=apply_fib):
        startstr = axiom
        endstr = ""
        for i in range(iters):
            endstr = process_string(startstr, func)
            startstr = endstr

        return endstr

    def process_string(oldstr, func):
        newstr = ""
        for char in oldstr:
            newstr = newstr + func(char)

        return newstr

    def draw(instructions, angle=60, distance=5):
        positions = []
        for i in instructions:
            if i == "F":
                t.forward(distance)
            elif i == "B":
                t.backward(distance)
            elif i == "-":
                t.left(angle)
            elif i == "+":
                t.right(angle)
            elif i == '[':
                positions.append([t.heading(),t.xcor(),t.ycor()])
            elif i == ']':
                position = positions.pop()
                t.setheading(position[0])
                t.setposition(position[1],position[2])
                
    def main(func):
        if func == "herb":
            instructions = create_rules("H", 5, apply_herb)
            draw(instructions, 25.7)
        elif func == "branch":
            instructions = create_rules("F", 5, apply_branch)
            draw(instructions, 25)
        else:
            t.forward(350)
            instructions = create_rules("F", 4, apply_fib)
            wn.setworldcoordinates(0,0,415,130)
            draw(instructions)
            print "It's a castle!"
        
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(20)
    t.up()
    t.backward(350)
    t.down()
    main(func)
    wn.exitonclick()
    

if __name__ == "__main__":
    l1 = [randrange(1000) for i in range(100)]
    l2 = [randrange(-100,100) for i in range(100)]
    #~ print average(l1)
    #~ maximum(l1)
    assert isprime(11) == True
    assert getprimes(12) == [2, 3, 5, 7, 11]
    assert squaresum([2, 3, 4]) == 29
    assert countodd([1,3,4,5,6,9]) == 4
    assert sumeven([1,3,8,4,5,6,9]) == 18
    assert sumnegative([-3,5,-7,9,-11]) == -21
    assert countlength(["nobody", "likes", "these", "long", "lists"]) == 3
    assert sumexclude([1,3,7,4,5]) == 11
    assert countinclude([1, "dick", 3, 9.5, "pi", "sam", 13, 1]) == 6
    list_methods()
    s = 'I love spom! Spom, spom, spom, yum!'
    assert replace('Mississippi', 'i', 'I') == 'MIssIssIppI'
    assert replace(s, 'om', 'am') == 'I love spam! Spam, spam, spam, yum!'
    assert replace(s, 'o', 'a') == 'I lave spam! Spam, spam, spam, yum!'
    assert getprimes_sieve(10) == [2,3,5,7]
    #~ turtle_lsys("branch")

#!/usr/bin/env python2
# *-* coding: utf-8 *-*

"Interactive Python Part 8: File Operations"

def withfor():
    qbfile = open("lib/qbdata.txt","r")
    for line in qbfile:
        values = line.split()
        print 'QB ', values[0], values[1], 'had a rating of ', values[10]
    qbfile.close()

def withwhile():
    infile = open("lib/qbdata.txt","r")
    line = infile.readline()
    while line:
        values = line.split()
        print 'QB ', values[0], values[1], 'had a rating of ', values[10]
        line = infile.readline()
    infile.close()

def withwith():
    with open("lib/qbdata.txt", "r") as f:
        for i in f:
            print i.strip()

def readwrite():
    with open("lib/qbdata.txt", "r") as f:
        # Read file into list.
        lst = list(f)
        # Go back to the top of the file, if we want to process it a second time.
        f.seek(0)
        # Read file into string. We could use ''.join(lst) here to skip seek.
        s = f.read()
    with open("lib/qbnew.txt", "w") as f:
        f.write(s)

def students():
    "Using the text file studentdata.txt write a program that prints out the\
    names of students that have more than six quiz scores."
    
    with open("lib/students.txt", "r") as f:
        for i in f:
            if len(i.split()) > 6:
                print i.strip()

def students_avg():
    """Using the text file studentdata.txt (shown in exercise 1) write a program
    that calculates the average grade for each student, and print out the student’s
    name along with their average grade."""
    
    with open("lib/students.txt", "r") as f:
        for i in f:
            line = i.split()
            avg = sum(float(i) for i in line[1:])/len(line)
            print "Name: %s, Avg: %.2f" % (line[0], avg)

def students_max():
    """Using the text file studentdata.txt (shown in exercise 1) write a program
    that calculates the minimum and maximum score for each student. Print out
    their name as well."""
    
    with open("lib/students.txt", "r") as f:
        for i in f:
            line = i.split()
            print "Name: %s, Min-Max: %s-%s" % (line[0], min(line[1:]), max(line[1:]))

def labdata():
    """Interpret the data file labdata.txt such that each line contains an x,y
    coordinate pair. Write a function called plotRegression that reads the data
    from this file and uses a turtle to plot those points and a best fit line
    according to the following formulas:
    y=y¯+m(x−x¯)
    m=∑xiyi−nx¯y¯∑x2i−nx¯2
    where x¯ is the mean of the x-values, y¯ is the mean of the y- values and n
    is the number of points. If you are not familiar with the mathematical ∑ it
    is the sum operation. For example ∑xi means to add up all the x values.
    Your program should analyze the points and correctly scale the window using
    setworldcoordinates so that that each point can be plotted.
    Then you should draw the best fit line, in a different color, through the points."""

    def plot(data):
        import turtle
        
        wn = turtle.Screen()
        t = turtle.Turtle()
        t.speed(1)

        # Set up our variables for the formula.
        x_lst, y_lst = [i[0] for i in data], [i[1] for i in data]
        x_sum, y_sum = float(sum(x_lst)), float(sum(y_lst))
        x_mean, y_mean = x_sum/len(x_lst), y_sum/len(y_lst)
        
        # Not sure about the formula where x and E are concerned ...
        m = ((x_sum*y_sum)-(20*x_mean*y_mean))/(x_sum**2-(20*x_mean**2))
        y = y_mean + m*(x_sum-x_mean) # This gives 966=x_sum so it can't be right.

        # Get min and max values for coordinate system.
        x_min, x_max, y_min, y_max = min(x_lst), max(x_lst), min(y_lst), max(y_lst)
        # Add 10 points on each line to be safe.
        wn.setworldcoordinates(x_min-10,y_min-10,x_max+10,y_max+10)

        for i in data:
            t.setpos(i[0], i[1])
        
        wn.exitonclick()
        
    with open("lib/labdata.txt") as f:
        coords = [map(int, line.split()) for line in f]
        
    plot(coords)

def mystery():
    """At the end of this chapter is a very long file called mystery.txt The
    lines of this file contain either the word UP or DOWN or a pair of numbers.
    UP and DOWN are instructions for a turtle to lift up or put down its tail.
    The pair of numbers are some x,y coordinates. Write a program that reads the
    file mystery.txt and uses the turtle to draw the picture described by the
    commands and the set of points."""

    import turtle
    
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(20)
    
    with open("lib/mystery.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line == "UP":
                t.up()
            elif line == "DOWN":
                t.down()
            else:
                x, y = map(int, line.split())
                t.setpos(x, y)

    wn.exitonclick()

def replace_newlines():
    "Small exercise to replace newlines and punctuation in a text file."
    from string import punctuation
    # Need to open with Ub mode as \r does not by default get converted to \n in
    # python2 so those line breaks would remain (and break the string joining process).
    with open("lib/alice_in_wonderland.txt", "Ub") as f:
        # Generally avoid .read() but in this case it doesn't matter as I'm generating
        # a huge string either way.
        # With .read()
        book1 = [" " if i in punctuation or i == "\n" else i for i in f.read()]
        
        # Line by line
        f.seek(0)
        book2 = []
        for line in f:
            line = ''.join([" " if i in punctuation or i == "\n" else i for i in line])
            book2.append(line)
        
        # Third option, should perform better, for more control, use a dict.
        f.seek(0)
        #~ unwanted={'\n':' ','.':' ',',':' ',':':' ','/':' ',"'":' '}
        unwanted=punctuation + "\n"
        def replace_characters(text, unwanted):
            for i in unwanted:
                text = text.replace(i, " ")
            return text
        book3 = []
        for line in f:
            book3.append(replace_characters(line, unwanted))

        # Make sure all three options return the same result.
        return ''.join(book1) == ''.join(book2) == ''.join(book3)


if __name__ == "__main__":
    #~ withfor()
    #~ withwhile()
    #~ withwith()
    #~ readwrite()
    #~ students()
    #~ students_avg()
    #~ students_max()
    #~ labdata()
    assert replace_newlines() == True
    mystery()

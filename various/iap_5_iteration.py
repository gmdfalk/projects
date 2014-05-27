#! /usr/bin/env python2

"Interactive Python Part 5: Iteration and Repetition"

import random
from lib import cImage as image

def wandering_turtle():
    """Modify the walking turtle program so that rather than a 90 degree left or
    right turn the angle of the turn is determined randomly at each step.
    Modify the turtle walk program so that you have two turtles each with a random
    starting location. Keep the turtles moving until one of them leaves the screen.
    Modify the previous turtle walk program so that the turtle turns around when
    it hits the wall or when one turtle collides with another turtle."""
    u = turtle.Turtle()
    u.shape("turtle")
    u.color("green")
    t.color("red")
    for i in [t, u]:
        i.penup()
        i.setpos(random.randrange(-300,300), random.randrange(-300,300))
        i.pendown()

    while True:
        for t1, t2 in [(t, u), (u, t)]:
            coin = random.randrange(2)
            angle = random.randrange(360)
            if coin:
                t1.left(angle)
            else:
                t1.right(angle)
            t1.forward(50)
            if t1.distance(0,0) > 390 or t1.distance(t2) < 25:
                t1.setpos(0,0)

def turtlebar_3n(n, old_n):
    colors = ("green", "blue", "red", "purple")
    color = random.choice(colors)
    t.fillcolor(color)
    wn.setworldcoordinates(0, 0, 400, 200)
    if t.distance(0,0) > 390:
        return
    t.begin_fill()
    t.write(old_n)
    t.left(90)
    t.forward(n)
    t.right(90)
    t.write(n)
    t.forward(10)
    t.right(90)
    t.forward(n)
    t.left(90)
    t.end_fill()

def sequence_3n(n=97):
    count = 0
    old_n = n
    while n != 1:
        if n % 2:
            n = n * 3 + 1
        else:
            n /= 2
        count += 1
    print old_n, "to", n, "after", count, "iterations"
    turtlebar_3n(count, old_n)
    return (count, old_n)

def highest_count(start=100, end=200):
    max_iters = 0
    for i in range(start, end):
        result = sequence_3n(i)
        if result[0] > max_iters:
            max_iters = result[0]
            max_value = result[1]
    print "Highest in range %s to %s was %s iterations for %s." % (start, end-1,
        max_iters, max_value)

def sqrt_newton(n):
    count = 0
    guess = 0.5 * n
    betterguess = 0.5 * (guess + n/guess)
    
    while betterguess != guess:
        guess = betterguess
        betterguess = 0.5 * (guess + n/guess)
        count += 1
    print count, "iterations for",
    return betterguess

def triangular(n=5):
    num = 0
    for i in range(1, n+1):
        num += i
        print num,

def isprime(n=936):
    """Write a function, is_prime, that takes a single integer argument and
    returns True when the argument is a prime number and False otherwise."""
    if n < 3: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#########################
# Image Setup Functions #
#########################

def setup_image(img_file):
    "Initialize image, get its size, draw a canvas and return these values"
    # Read the image from the file.
    oldimg = image.Image(img_file)
    # And create a duplicate under newimg.
    newimg = oldimg.copy()
    # Map out width and height to display our image in.
    width, height = oldimg.getWidth(), oldimg.getHeight()
    win = image.ImageWin(img_file, width, height)
    
    return oldimg, newimg, width, height, win
    
def write_image(img_file, newimg, win, func_name):
    "Draw and save a processed image"
    # This order will only save if the window gets clicked on.
    newimg.draw(win)
    win.exitonclick()
    img_name, img_ext = strip_name(img_file)
    newimg.save(img_name+func_name+img_ext)

def strip_name(img_file):
    "Strips the name of a file into (pathname, extension)"
    from os.path import splitext
    return splitext(img_file)

##############################
# Image Standalone Functions #
##############################

def invert_image(img_file="cy.png"):
    oldimg, newimg, width, height, win = setup_image(img_file)
    
    for col in range(newimg.getWidth()):
        for row in range(newimg.getHeight()):
            p = newimg.getPixel(col,row)
            p.red = 255 - p.red
            p.green = 255 - p.green
            p.blue = 255 - p.blue
            newimg.setPixel(col,row,p)

    write_image(img_file, newimg, win, "_inv")
    
def greyscale_image(img_file="cy.png"):
    "Write a function to convert the image to grayscale."
    oldimg, newimg, width, height, win = setup_image(img_file)
    
    for col in range(newimg.getWidth()):
        for row in range(newimg.getHeight()):
            p = newimg.getPixel(col,row)
            avg = (p[0]+p[1]+p[2])/3
            p.red = p.green = p.blue = avg
            newimg.setPixel(col,row,p)

    write_image(img_file, newimg, win, "_grey")
    
def blackwhite_image(img_file="cy.png"):
    "Write a function to convert an image to black and white."
    oldimg, newimg, width, height, win = setup_image(img_file)
    
    for col in range(newimg.getWidth()):
        for row in range(newimg.getHeight()):
            p = newimg.getPixel(col,row)
            avg = (p[0]+p[1]+p[2])/3
            if avg >= 128:
                avg = 255
            else:
                avg = 0
            p.red = p.green = p.blue = avg
            newimg.setPixel(col,row,p)

    write_image(img_file, newimg, win, "_bw")

def remred_image(img_file="cy.png"):
    "Write a function to remove all the red from an image."
    oldimg, newimg, width, height, win = setup_image(img_file)
    
    for col in range(newimg.getWidth()):
        for row in range(newimg.getHeight()):
            p = newimg.getPixel(col,row)
            p.red = 0
            newimg.setPixel(col,row,p)

    write_image(img_file, newimg, win, "_nored")

def sepia_image(img_file="cy.png"):
    """Sepia Tone images are those brownish colored images that may remind you
    of times past. The formula for creating a sepia tone is as follows:
    newR = (R × 0.393 + G × 0.769 + B × 0.189)
    newG = (R × 0.349 + G × 0.686 + B × 0.168)
    newB = (R × 0.272 + G × 0.534 + B × 0.131)
    Write a function to convert an image to sepia tone. Hint: Remember that rgb
    values must be integers between 0 and 255."""
    
    oldimg, newimg, width, height, win = setup_image(img_file)
    
    for col in range(newimg.getWidth()):
        for row in range(newimg.getHeight()):
            try:
                p = newimg.getPixel(col,row)
                p.red = int(p.red * 0.393 + p.green * 0.769 + p.blue * 0.189)
                p.green = int(p.red * 0.349 + p.green * 0.686 + p.blue * 0.168)
                p.blue = int(p.red * 0.272 + p.green * 0.534 + p.blue * 0.131)
                newimg.setPixel(col,row,p)
            except:
                continue

    write_image(img_file, newimg, win, "_sepia")
    
def double_image(img_file="cy.png"):
    "Write a function to uniformly enlarge an image by a factor of 2 (double the size)."

    # FIXME: Need to assign two values to unused_ here as this function needs
    # two different (*2) values in their place.
    oldimg, unused_newimg, width, height, unused_win = setup_image(img_file)
    newimg = image.EmptyImage(width*2, height*2)
    win = image.ImageWin(img_file, width*2, height*2)

    for row in range(height):
        for col in range(width):    
            oldpixel = oldimg.getPixel(col,row)
            newimg.setPixel(2*col,2*row, oldpixel)
            newimg.setPixel(2*col+1, 2*row, oldpixel)
            newimg.setPixel(2*col, 2*row+1, oldpixel)
            newimg.setPixel(2*col+1, 2*row+1, oldpixel)

    write_image(img_file, newimg, win, "_double")

def smooth_image(img_file="cy_double.png"):
    """After you have scaled an image too much it looks blocky. One way of reducing
    the blockiness of the image is to replace each pixel with the average values
    of the pixels around it. This has the effect of smoothing out the changes in
    color. Write a function that takes an image as a parameter and smooths the
    image. Your function should return a new image that is the same as the old
    but smoothed."""
    
    oldimg, newimg, width, height, win = setup_image(img_file)

    for col in range(newimg.getWidth()):
        for row in range(newimg.getHeight()):
            p = newimg.getPixel(col, row)
            neighbors = []
            # Put the 8 surrounding pixels into neighbors
            for i in range(col-1, col+2):
                for j in range(row-1, row+2):
                    try:
                        neighbor = newimg.getPixel(i, j)
                        neighbors.append(neighbor)
                    except:
                        continue
            nlen = len(neighbors)
            # Average out the RBG values
            if nlen:
            # Uncommented, the following line would leave most of the white 
            # untouched which works a little better for real photographs, imo.
            #~ if nlen and p[0]+p[1]+p[2] < 690:
                p.red = sum([neighbors[i][0] for i in range(nlen)])/nlen
                p.green = sum([neighbors[i][1] for i in range(nlen)])/nlen
                p.blue = sum([neighbors[i][2] for i in range(nlen)])/nlen
                newimg.setPixel(col,row,p)

    write_image(img_file, newimg, win, "_smooth")


#################################
# Functions belonging to pixmap #
#################################

def nored(p, *args):
    p = image.Pixel(0, p.green, p.blue)
    return p
    
def grey(p, *args):
    avg = (p.red + p.green + p.blue)/3
    p = image.Pixel(avg, avg, avg)
    return p

def median(p, col, row):
    """When you scan in images using a scanner they may have lots of noise due
    to dust particles on the image itself or the scanner itself, or the images
    may even be damaged. One way of eliminating this noise is to replace each
    pixel by the median value of the pixels surrounding it."""
    neighbors = []
    # Put the 8 surrounding pixels into neighbors
    for i in range(col-1, col+2):
        for j in range(row-1, row+2):
            try:
                neighbor = newimg.getPixel(i, j)
                neighbors.append(neighbor)
            except:
                continue
    nlen = len(neighbors)
    if nlen:
        red = [neighbors[i][0] for i in range(nlen)]
        green = [neighbors[i][1] for i in range(nlen)]
        blue = [neighbors[i][2] for i in range(nlen)]
        # Sort the lists so we can later find the median.
        for i in [red, green, blue]:
            i.sort()
        # If the list has an odd number of items in it.
        if nlen % 2:
            p.red = red[len(red)/2]
            p.green = green[len(green)/2]
            p.blue = blue[len(blue)/2]
        else:
            p.red = (red[len(red)/2] + red[len(red)/2-1])/2
            p.green = (green[len(green)/2] + green[len(green)/2-1])/2
            p.blue = (blue[len(blue)/2] + blue[len(blue)/2-1])/2   

    return p
    
def pixmap(img_file="cy.png", func=nored):
    """Write a general pixel mapper function that will take an image and a pixel
    mapping function as parameters. The pixel mapping function should perform a
    manipulation on a single pixel and return a new pixel."""
    
    oldimg, blank, width, height, win = setup_image(img_file)

    newimg = image.EmptyImage(width,height)

    for col in range(width):
        for row in range(height):
            p = oldimg.getPixel(col, row)
            new_p = func(p, col, row)
            newimg.setPixel(col, row, new_p)

    newimg.draw(win)
    img_name, img_ext = strip_name(img_file)
    # Func.__name__ probably will produce unwanted results here if using
    # decorators or mocking the function but for now, we're leaving it.
    newimg_name = img_name + "_" + func.__name__ + img_ext
    newimg.save(newimg_name)

    win.exitonclick()

#############
# Main Body #
#############

if __name__ == "__main__":

    #~ print sqrt_newton(25)
    #~ highest_count(100, 10000)
    #~ triangular(10)
    #~ for i in range(20):
        #~ print i, isprime(i)

    #~ import turtle
    #~ wn = turtle.Screen()
    #~ t = turtle.Turtle()
    #~ t.shape("turtle")
    #~ wandering_turtle()
    #~ for i in range(150,200):
        #~ sequence_3n(i)
        
    #~ invert_image()
    #~ greyscale_image()
    #~ remred_image()
    #~ blackwhite_image()
    #~ sepia_image()
    #~ smooth_image()
    double_image()
    pixmap("cy_double.png", grey)

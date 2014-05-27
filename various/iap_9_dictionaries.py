#!/usr/bin/env python2
# *-* coding: utf-8 *-*

"Interactive Python Part 9: Dictionaries"

def count_all(s):
    """Define the function to require one parameter, the string.
    Create an empty dictionary of counts.
    Iterate through the characters of the string, one character at a time.
    Return a dictionary with the count of each char.
    Count the number of times each letter occurs. Keep the count in a dictionary."""
    # Initial version.
    #~ count_dict = {}
    #~ for i in s:
        #~ if i in count_dict:
            #~ count_dict[i] += 1
        #~ else:
            #~ count_dict[i] = 1
    #~ return count_dict
    
    # The beauty of python.
    #~ return {key: s.count(key) for key in s}

    # With sorting. Since we cannot sort a dict we'll have to translate to list.
    import operator
    d = {key: s.count(key) for key in s}
    return sorted(d.iteritems(), key=operator.itemgetter(1))

def count_all_collections(s):
    # The smart way. Incidentally, this performs much better than any of the above.
    from collections import Counter
    return Counter(s)

def create_bar(s):
    """Get the keys from the dictionary, convert them to a list, and sort them.
    Iterate through the keys, in alphabetical order, getting the associated value (count).
    Make a histogram bar for each."""
    
    import turtle
    import random

    # Turtle setup
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("green")
    wn.setworldcoordinates(0,0,400,200)
    colors = ("green", "blue", "red", "purple", "orange", "gray", "brown")
    
    # Get the sorted dictionary.
    key_list = count_all(s)
    

    for key, value in key_list:
        color = random.choice(colors)
        t.fillcolor(color)
        t.begin_fill()
        t.left(90)
        t.forward(value*10)
        t.right(90)
        t.forward(5)
        t.write(key)
        t.forward(10)
        t.write(value)
        t.forward(5)
        t.right(90)
        t.forward(value*10)
        t.left(90)
        t.end_fill()
    wn.exitonclick()

def counted_table(s):
    """Write a program that reads in a string on the command line and returns a
    table of the letters of the alphabet in alphabetical order which occur in
    the string together with the number of times each letter occurs. Case should
    be ignored."""
    import operator
    from string import lowercase

    # Possibility 1 with operator.
    d = {i: s.count(i) for i in s if i in lowercase}
    sorted_d = sorted(d.iteritems(), key=operator.itemgetter(0))
    for i in sorted_d:
        print i[0], i[1]

    # Possibility 2 without import.
    keys = d.keys()
    keys.sort()
    for char in keys:
        print char, d[char]

def makeitwork():

    def add_fruit(inventory, fruit, quantity=0):
        if fruit in inventory:
            inventory[fruit] += quantity
        else:
            inventory[fruit] = quantity
        print inventory

    # Make these tests work...
    new_inventory = {}
    add_fruit(new_inventory, 'strawberries', 10)
    assert ('strawberries' in new_inventory) == True
    assert new_inventory['strawberries'] == 10
    add_fruit(new_inventory, 'strawberries', 25)
    assert new_inventory['strawberries'] == 35

def alice_in_wonderland():
    """How many times does the word, alice, occur in the book? If you are writing
    this in the activecode window simply print out the results rather than write
    them to a file.
    What is the longest word in Alice in Wonderland? How many characters does it have?"""
    from collections import Counter
    with open("lib/alice_in_wonderland.txt") as f:
        #~ table = maketrans(" "," ")
        #~ wordlist = f.read().lower().translate(table, punctuation).split()
        # Translate actually performs fastest here but we use list comprehension
        # because we like it.
        wordlist = [i.lower() for i in f.read().split() if i.isalpha()]
        counted_words = Counter(wordlist)
    # Sort and write our counted wordlist to a new file:
    with open("lib/alice_counted.txt", "w") as fout:
        length = 0
        for k, v in sorted(counted_words.items()):
            if len(k) > length:
                length = len(k)
                print length
            fout.write(k + " " + str(v) + "\n")

        # 3 Solutions for counting characters (not words):
        #~ import operator
        #~ from string import lowercase, punctuation
        
        # 1: Reading the file into a string, then performing dictionary comprehension.
        #~ s = f.read().lower()
        #~ # Incredibly stupid and slow because it goes through the whole string
        #~ # with each iteration. DO NOT DO THIS.
        #~ L = {i: s.count(i) for i in s if i in lowercase}
        #~ L_sorted = sorted(L.iteritems(), key=operator.itemgetter(0))
        #~ print L_sorted

        # 2: Reading the file line by line into a dictionary.
        #~ d = {}
        #~ for i in f:
            #~ i = i.lower().strip()
            #~ i = [c for c in i if c in lowercase]
            #~ for char in i:
                #~ if char in d:
                    #~ d[char] += 1
                #~ else:
                    #~ d[char] = 1
        #~ keys = d.keys()
        #~ keys.sort()
        #~ for i in keys:
            #~ print (i, d[i]),

        # 3: Using Counter
        #~ s = [i for i in f.read().lower() if i in lowercase]
        #~ d = Counter(s)
        # Long version:
        #~ keys = sorted(d.keys())
        #~ for i in keys:
            #~ print (i, d[i]),
        #~ # Concise:
        #~ for k, v in sorted(d.items()): print (k, v),

def pirate():
    """Write a program that asks the user for a sentence in English and then
    translates that sentence to Pirate."""
    
    from random import choice
    d = {
        "sir": "matey", "hotel": "fleabag inn", "student": "swabbie",
        "boy": "matey", "girl": "wench", "professor": "foul blaggart",
        "restaurant": "galley", "your": "ye", "excuse": "arr", "you": "ye",
        "students": "swabbies", "are": "be", "lawyer": "foul blaggart",
        "the": "th'", "restroom": "head", "my": "me", "hello": "avast",
        "is": "be", "man": "scurvy dog", "hey": "avast", "pirate": "scurvy pirate",
        "idiot": "flunder", "young": "ye", "the": "t'", "suck": "blow down",
        "fall": "hade", "happens": "be happening", "death": "Davy Jones' treasure chest",
        "always": "ever", "you're": "ye're", "girlfriend": "Lassie-Lucy",
        "with": "wit'", "everyone": "evr'un"
        }
    #~ sentence = raw_input("What be yer sentence, ye old landlubber? ")
    sentences = ["If the world didn't suck we'd all fall off",
                "What happens if you get scared half to death twice?",
                "Save water and shower with your girlfriend",
                "Always remember you're unique, just like everyone else"]
    
    start = ["Yarr, ", "Yarr! ", "Yarr-ha-harr! ", "Skuttle me Skippers! ",
             "Shiver me timbers! ", "Ahoy, me hearties! ", "Dogs ahoy! ",
             "Hoist the mizzen!!! ", "Hoist the colors!! " ]
    end = [". ARRRGHHHH!", ". Avast ye varmint!", ". Yarr?",
           ". Savvyy?", ". Yarr!", ". Aye!",
           ", ye bilge rat!", ", ye mangy dog!", ", ye scallywag!"]

    s = choice(sentences)
    print s
    print choice(start) +\
          ' '.join([d[i] if i in d else i for i in s.lower().split()]).capitalize()\
          + choice(end)
            
if __name__ == "__main__":
    #~ s = "i like pie, it's very nice, yes indeed, it is. banana"
    #~ print count_all(s)
    #~ create_bar(s)
    #~ counted_table(s)
    #~ makeitwork()
    #~ alice_in_wonderland()
    pirate()

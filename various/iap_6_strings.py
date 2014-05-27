#!/usr/bin/env python2
# *-* coding: utf-8 *-*

"Interactive Python Part 6: Strings"

vowels = "aeiouAEIOU"
# Without recursion.
def remove_vowels(s):
    return ''.join([i for i in s if i not in vowels])

# With recursion, for fun and profit. Actually, not so much profit as iteration
# and list comprehension are typically the better choice.
# Python has no tail-call elimination (TCE) which makes recursion unable to
# handle large data. And as we all know, Big Data is the future ~~
def recurse_vowels(s):
    "Final version, without the use of a second variable."
    if not s:
        return ""
    elif s[0] in vowels:
        return recurse_vowels(s[1:])
    else:
        return s[0] + recurse_vowels(s[1:])
    
def recurse_vowels_2(s, new_s=""):
    if not s:
        return new_s
    elif s[0] not in vowels:
        new_s += s[0]

    return recurse_vowels_2(s[1:], new_s)

def recurse_vowels_3(s, new_s=""):
    if not s:
        return new_s
    elif s[0] in vowels:
        return recurse_vowels_3(s[1:], new_s)
    else:
        return recurse_vowels_3(s[1:], new_s + s[0])

def recurse_vowels_4(s, lst=None):
    "Initial version, before refactoring."
    if lst is None:
        lst = []
    if not len(s):
        return ''.join(lst)
    else:
        if s[0] in vowels:
            return recurse_vowels_4(s[1:], lst)
        lst.append(s[0])
        return recurse_vowels_4(s[1:], lst)

def lsys(iters=5):
    "Displaying the Lindenmayer system."
    a, b = "A", "B"
    olda = a
    for i in range(iters):
        print i, len(a),
        print a,
        print b
        a, b = a+b, a

# Since lsys is essentially a fibbonacci sequence, here is a recursive function
# that returns the nth number in the sequence.
def fib(n):
    if n < 2: return 1
    return fib(n-2) + fib(n-1)

def turtle_lsys(func="fib"):
    import turtle
        
    def apply_fib(char):
        newstr = ""
        if char == "F":
            newstr = "F-F++F-F"
        else:
            newstr = char
            
        return newstr
        
    def apply_hilbert(char):
        newstr = ""
        if char == "L":
            newstr = "+RF-LFL-FR+"
        elif char == "R":
            newstr = "-LF+RFR+FL-"
        else:
            newstr = char
            
        return newstr
        
    def apply_dragon(char):
        newstr = ""
        if char == "X":
            newstr = "X+YF+"
        elif char == "Y":
            newstr = "-FX-Y"
        else:
            newstr = char
            
        return newstr

    def apply_arrow(char):
        newstr = ""
        if char == "X":
            newstr = "YF+XF+Y"
        elif char == "Y":
            newstr = "XF-YF-X"
        else:
            newstr = char
            
        return newstr

    def apply_peano(char):
        newstr = ""
        if char == "X":
            newstr = "X+YF++YF-FX--FXFX-YF+"
        elif char == "Y":
            newstr = "-FX+YFYF++YF+FX--FX-Y"
        else:
            newstr = char
            
        return newstr

    def apply_sierpinski(char):
        newstr = ""
        if char == "F":
            newstr = "FF"
        elif char == "X":
            newstr = "--FXF++FXF++FXF--"
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
        for i in instructions:
            if i == "F":
                t.forward(distance)
            elif i == "B":
                t.backward(distance)
            elif i == "-":
                t.left(angle)
            elif i == "+":
                t.right(angle)
                
    def main(func):
        if func == "hilbert":
            instructions = create_rules("LR", 4, apply_hilbert)
            draw(instructions, 90)
        elif func == "dragon":
            instructions = create_rules("FX", 8, apply_dragon)
            draw(instructions, 90)
        elif func == "arrowhead":
            instructions = create_rules("YF", 6, apply_arrow)
            draw(instructions)
        elif func == "peano":
            instructions = create_rules("FX", 6, apply_peano)
            draw(instructions)        
        elif func == "sierpinski":
            instructions = create_rules("FXF--FF--FF", 4, apply_sierpinski)
            draw(instructions)
        else:
            instructions = create_rules("F", 4, apply_fib)
            wn.setworldcoordinates(0,0,415,130)
            draw(instructions)
            print "It's a castle!"
        
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(20)
    main(func)
    wn.exitonclick()

def count_letter(word, letter, count=0):
    for char in word.lower():
        if char == letter:
            count += 1
    return (count, letter)

def count_recursive(word, letter, count=0):
    if not len(word):
        return (count, letter)
    if letter in word[0].lower():
        count += 1
    return count_recursive(word[1:], letter, count)

def find_char(word, char, occurrence=1, start=0, end=None):
    if end is None:
        end = len(word)
    count = 0
    for i in range(start, end):
        if word[i] == char:
            count += 1
            if occurrence == count:
                return i
    return -1

def check_quote():
    """Assign to a variable in your program a triple-quoted string that contains
    your favorite paragraph of text - perhaps a poem, a speech, instructions to
    bake a cake, some inspirational verses, etc.
    Write a function that counts the number of alphabetic characters (a thru z,
    or A thru Z) in your text and then keeps track of how many are the letter ‘e’."""
    
    import string
    
    quote = """Der Mond verbirgt sein bleiches Licht,
die Sterne am Himmel, sie funkeln nicht.
Die Nacht ist schwül.
Im Herzen wird band.
Der Uhu krächzt einen Totengesang.

Da - bricht`s aus schwarzer Nacht hervor,
äls wäre geöffnet der Hölle Tor,
als ständen die Säulen des Erdballs in Flammen,
äls stürze das ganze Weltall zusammen,
und aus der Wolken feuchtem Schoß
der Regen in Strömen sich ringsum ergoss,
als wollten des Wassers wilde Gewalten
das Land zum unendlichen Meere gestalten.

Und wie es stürmt und brandet und kracht,
da, eine Jungfrau tritt hinaus in die Nacht
und ruft in die tosenden Winde hinaus:
'Na, das ist ein Dreckwetter, da bleib ich zuhaus!'"""

    print quote
    found = count_letter(quote, "e")
    length = sum(1 for i in quote if i in string.letters)
    print "\nYour text contains %s alphabetic characters, of which %s (%.02f%%) are '%s'."\
        % (length, found[0], float(length)/found[0], found[1])

def mult_table(x=10, y=10):
    "Print out a neatly formatted multiplication table, up to 12 x 12."
    x += 1
    y += 1
    table = [i*j for i in range(x) for j in range(y)]
    start, end = 0, x
    for i in range(x):
        print i, table[start:end]
        start, end = end, end+x

def int_digits(n):
    "Write a function that will return the number of digits in an integer"
    return len(str(n))

def reverse_string(s):
    "Write a function that reverses its string argument."
    return s[::-1]

def mirror(s):
    "Write a function that mirrors its argument."
    return s+s[::-1]

def recurse_mirror(s, olds=""):
    """Attempt at mirror() recursively though i'm failing. olds gets pushed onto
    the stack before the final return value collection so the order of olds and s
    is reversed."""
    if not s:
        return olds
    elif olds < s:
        olds = s
    return s[-1] + recurse_mirror(s[:-1], olds)

def countdown(n):
    "Write a function that counts down to 0."
    for i in range(n, -1, -1):
    #~ for i in range(n+1)[::-1]:
    #~ for i in reversed(range(n+1)):
        print i,
    return "boom"

def recurse_countdown(n):
    if n < 1:
        return "boom"
    print n,
    return recurse_countdown(n-1)

def remove_letter(s, char):
    "Write a function that removes all occurrences of a given letter from a string."
    return ''.join([i for i in s if i != char])

def remove_letter_recurse(s, char):
    if not s:
        return ""
    elif s[0] == char:
        return remove_letter_recurse(s[1:], char)
    return s[0] + remove_letter_recurse(s[1:], char)

def palindrome(s):
    "Write a function that recognizes palindromes."
    return s == s[::-1]

def palindrome_recurse(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return palindrome_recurse(s[1:-1])
    return False

def count_substring(s, ss):
    "Write a function that counts how many times a substring occurs in a string."
    return s.count(ss)

def remove_substring(s, ss):
    "Write a function that removes the first occurrence of a string from another string."
    start = s.index(ss)
    if not start: return s
    result = s[:start] + s[start+len(ss):]
    return result
    
def remove_substrings(s, ss):
    "Write a function that removes all occurrences of a string from another string."
    return s.replace(ss, "")

def encrypt(message, mapping):
    """Write a function that implements a substitution cipher. In a substitution
    cipher one letter is substituted for another to garble the message.
    For example A -> Q, B -> T, C -> G etc. your function should take two
    parameters, the message you want to encrypt, and a string that represents the
    mapping of the 26 letters in the alphabet. Your function should return a
    string that is the encrypted version of the message."""
    # It's late and i opted for the lazy version:
    return ''.join([chr(ord(i)+mapping) for i in message])

def decrypt(message, mapping):
    return ''.join([chr(ord(i)-mapping) for i in message])

def remove_dups(s):
    """Write a function called removeDups that takes a string and creates a new
    string by only adding those characters that are not already present.
    In other words, there will never be a duplicate letter added to the new string."""
    # FIXME: Do it the long way, too.
    return ''.join(set(s))

def rot13(message, action="encode"):
    """Write a function called rot13 that uses the Caesar cipher to encrypt a
    message. The Caesar cipher works like a substitution cipher but each character
    is replaced by the character 13 characters to ‘its right’ in the alphabet.
    So for example the letter a becomes the letter n. If a letter is past the
    middle of the alphabet then the counting wraps around to the letter a again,
    so n becomes a, o becomes b and so on."""
    from string import ascii_lowercase as lc
    new_message = ""
    message = message.lower()
    if action == "decode":
        for char in message:
            if char in lc:
                idx = (lc.index(char)-13) % 26
                new_message += lc[idx]
            else:
                new_message += char
        return new_message
    for char in message:
        if char in lc:
            idx = (lc.index(char)+13) % 26
            new_message += lc[idx]
        else:
            new_message += char
    return new_message

if __name__ == "__main__":
    #~ lsys()
    #~ turtle_lsys("sierpinski")
    #~ turtle_lsys()
    #~ check_quote()
    #~ mult_table()
    assert remove_vowels("TEsitIOUStriiNgUadE") == "TstStrNgd"
    assert recurse_vowels("TEsit.aAa.StriiNgUadA") == "Tst..StrNgd"
    assert fib(10) == 89
    assert count_letter("TEsit.IOU.StriiNgUadE", "i") == (4, "i")
    assert count_recursive("TEsit.IOU.StriiNgUadE", "i") == (4, "i")
    assert find_char("TEsit.IOU.StriiNgUadE", "E", 2) == 20
    assert int_digits(100) == 3
    assert reverse_string("popocatepetl") == "ltepetacopop"
    assert mirror("good") == "gooddoog"
    #~ assert recurse_mirror("good") == "dooggood" # FIXME
    assert recurse_countdown(10) == "boom"
    assert countdown(10) == "boom"
    assert remove_letter("this is a sentence", "s") == "thi i a entence"
    assert remove_letter_recurse("this is a sentence", "s") == "thi i a entence"
    assert palindrome("palindrome") == False
    assert palindrome_recurse("racecar") == True
    assert count_substring("asdfklasoeasoasas", "as") == 5
    assert remove_substring("aasdfklasoeasoasas", "as") == "adfklasoeasoasas"
    assert remove_substring("jkloe", "kl") == "joe"
    assert remove_substrings("aasdfklasoeasoasas", "as") == "adfkloeo"
    assert encrypt("this is a test", 3) == "wklv#lv#d#whvw"
    assert decrypt("wklv#lv#d#whvw", 3) == "this is a test"
    assert remove_dups("asdfasdfasdf") == "asdf"
    assert rot13("guvf vf n grfg, bxnl?", "decode") == "this is a test, okay?"
    assert rot13("this is a test, okay?") == "guvf vf n grfg, bxnl?"


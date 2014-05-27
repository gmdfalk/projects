#!/usr/bin/env python2

# Pig Latin is a game of alterations played on the English language game.
# To create the Pig Latin form of an English word the initial consonant sound
# is transposed to the end of the word and an ay is affixed (Ex.: "banana"
# would yield anana-bay). Read Wikipedia for more information on rules.

def convert_word(arg):
    vowels = list("aeiouAEIOU")
    for i in enumerate(arg):
        if i[1] in vowels:
            print arg[i[0]:]+arg[:i[0]]+"ay"
            break

convert_word("piglatin")

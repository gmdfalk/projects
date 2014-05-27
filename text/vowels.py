#!/usr/bin/env python2

# Enter a string and the program counts the number of vowels in the text.
# For added complexity have it report a sum of each vowel found.

import re

def check_word(arg):
    vowels = "AEIOUaeiou"
    # Using comprehension:
    print sum(1 for c in arg if c in vowels)
    print [c for c in arg if c in vowels]
    # And the same, using regex:
    match_vowels = re.findall('[aeiou]', arg, re.IGNORECASE)
    print len(match_vowels)
    print match_vowels
        

check_word("AsdFeJklO")

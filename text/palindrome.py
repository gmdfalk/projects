#!/usr/bin/env python2

# Checks if the string entered by the user is a palindrome.
# That is that it reads the same forwards as backwards like “racecar”.

import string
import re

s = "A man, a plan, a canal: Panama!".lower()

# Only take actual letters into account.
s_stripped = "".join(c for c in s if c in string.letters)
# The same, using regex. string.letters is probably preferrable.
s_stripped = "".join(re.findall("[A-Za-z]", s))

if s_stripped == s_stripped[::-1]:
    print "'%s' is a palindrome!" % s
else:
    print "Sorry, '%s' is not a palindrome." % s

#!/usr/bin/env python2
# Print out the 2^n possibilities of a word with the length n 

import unittest
from itertools import product, permutations

def word_variations(s):
    try:
        if not len(s): return
        lower, upper = s.lower(), s.upper()
    except:
        return
    # Since number strings won't produce cartesian values with lower/upper,
    # we use itertools.permutations.
    if lower == upper:
        pairs = permutations(lower)
    else:
        pairs = product(*zip(lower, upper))
    result = {''.join(pair) for pair in pairs} # Using set literal notation.
    print result, "\n", len(result)
    return result

word_variations("abc")

class WordTest(unittest.TestCase):

    def _test(self, s, expected):
        result = word_variations(s)
        self.assertEqual(len(result), expected)

    def test_basecase(self):
        self._test("hello", 32)

    def test_int(self):
        self._test("123", 6)
        
    def test_empty(self):
        self.assertEqual(word_variations(""), None)

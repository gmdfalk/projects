#!/usr/bin/env python2

#~ import pdb
import unittest
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def perfect_square(n):
    x = 0
    try:
        int(n)
    except (ValueError, TypeError):
        logger.debug("Need an integer!")
        return
    if n >= 0:
        while x <= n:
            result = x*x
            if result == n:
                logger.debug("%s is a perfect square of %s!", x, n)
                return x
            else:
                x += 1
    elif n < 0:
        logger.debug("Sorry, not going to bother with complex numbers!")
        return
    logger.debug("There is no perfect square for %s", n)

def farmyard_problem(heads, legs):
    """
    There are x heads and y legs. How many chickens and pigs are on the farm?
    Brute-Forcing is often the easiest solution for these problems
    """
    
    chickens = heads
    pigs = 0
    for i in range(heads):
        if chickens*2 + pigs*4 == legs:
            logger.info("There are %s chickens and %s pigs!", chickens, pigs)
            return (chickens, pigs)
        else:
            chickens -= 1
            pigs += 1
    return (None, None)

print perfect_square(16)
print farmyard_problem(22, 56)    

class SquareTest(unittest.TestCase):

    def setUp(self):
        "twisted.trial only?"
        pass

    def _test(self, n, expected):
        result = perfect_square(n)
        self.assertEqual(result, expected)

    def test_positive(self):
        self._test(16, 4)
        
    def test_zero(self):
        self._test(0, 0)
        
    def test_negative(self):
        self._test(-200, None)
        
    def test_nonperfect(self):
        self._test(15, None)

    # Note, don't bother testing types, rather let Python handle the exception
    # or handle it yourself.
    # Keywords: Separation of Concerns, LBYL, EAFP
    #~ def test_exception(self):
        #~ self.assertRaises(ValueError, perfect_square, "foo")
        #~ self.assertRaises(TypeError, perfect_square, [8, 2])
        #~ self.assertRaises(TypeError, perfect_square, {"e": 3})

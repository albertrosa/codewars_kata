from __future__ import division
import unittest


def invert(lst):
    inverted = []
    for number in lst:
        inverted.append(number * -1)

    return inverted


class TestInvert(unittest.TestCase):

    def test_invert(self):
        self.assertEquals(invert([1, 2, 3, 4, 5]), [-1, -2, -3, -4, -5])
        self.assertEquals(invert([1, -2, 3, -4, 5]), [-1, 2, -3, 4, -5])
        self.assertEquals(invert([]), [])
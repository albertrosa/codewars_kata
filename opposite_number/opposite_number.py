from __future__ import division
import unittest


def opposite(number):
    return number * -1


class TestOppositeNumber(unittest.TestCase):

    def test_opposite_number(self):
        self.assertEquals(opposite(1), -1)
from __future__ import division
import unittest


def narcissistic(value):
    val = str(value)
    pwer = len(val)

    total = 0
    for number in val:
        total += int(number) ** pwer

    return value == total


class TestNarcissistic(unittest.TestCase):

    def test_narcissistic(self):
        self.assertEquals(narcissistic(7), True, '7 is narcissistic')
        self.assertEquals(narcissistic(371), True, '371 is narcissistic')
        self.assertEquals(narcissistic(122), False, '122 is not narcissistic')
        self.assertEquals(narcissistic(4887), False, '4887 is not narcissistic')

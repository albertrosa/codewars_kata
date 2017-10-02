from __future__ import division
import unittest


def find_average(array):
    total = 0
    for num in array:
        total += num

    if len(array):
        return total / len(array)
    else:
        return


class TestBMI(unittest.TestCase):

    def test_bmi(self):
        array = [1, 2, 3]
        self.assertEqual(find_average(array), 2)

        array = []
        self.assertEqual(find_average(array), 0)
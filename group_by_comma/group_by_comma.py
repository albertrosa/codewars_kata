from __future__ import division
import unittest


def group_by_commas(n):
    final_numbers = []

    numbers = list(str(n))
    numbers.reverse()

    if numbers.__len__() < 4:
        return str(n)

    i = 0
    while i < numbers.__len__():
        if i % 3 == 0:
            final_numbers.append(",")

        final_numbers.append(numbers[i])
        i += 1

    final_numbers.reverse()
    if final_numbers[final_numbers.__len__()-1] == ',':
        del(final_numbers[final_numbers.__len__()-1])

    return "".join(final_numbers)


class TestGoodVsEvil(unittest.TestCase):

    def test_good_vs_evil(self):
        self.assertEquals(group_by_commas(1), '1')
        self.assertEquals(group_by_commas(10), '10')
        self.assertEquals(group_by_commas(100), '100')
        self.assertEquals(group_by_commas(1000), '1,000')
        self.assertEquals(group_by_commas(10000), '10,000')
        self.assertEquals(group_by_commas(100000), '100,000')
        self.assertEquals(group_by_commas(1000000), '1,000,000')
        self.assertEquals(group_by_commas(35235235), '35,235,235')




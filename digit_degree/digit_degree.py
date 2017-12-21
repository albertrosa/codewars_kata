from __future__ import division
import unittest


def digitDegree(n):

    numbers = list(str(n))
    iterations = 0

    print(numbers)

    while numbers.__len__() > 1:
        current_sum = 0
        for number in numbers:
            current_sum += int(number)

        numbers = list(str(current_sum))
        iterations += 1

    return iterations


class TestDigitDegree(unittest.TestCase):

    def test_digit_degree(self):

        self.assertEquals(digitDegree(5), 0)
        self.assertEquals(digitDegree(100), 1)
        self.assertEquals(digitDegree(91), 2)




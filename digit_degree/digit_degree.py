from __future__ import division
import unittest


def digitDegree(n):

    # Convert the number to an array of strings
    numbers = list(str(n))

    # used to keep track of iterations
    iterations = 0

    # we will only need to iterate if there is more than one digit.
    while numbers.__len__() > 1:
        # used to store the new number after summation of the original number
        current_sum = 0

        # here we loop through the array in order to obtain the new summation
        for number in numbers:
            current_sum += int(number)

        # here we store the new number array based on the summation
        numbers = list(str(current_sum))
        # here we increment the iteration to keep track of loop
        iterations += 1

    return iterations


class TestDigitDegree(unittest.TestCase):

    def test_digit_degree(self):

        self.assertEquals(digitDegree(5), 0)
        self.assertEquals(digitDegree(100), 1)
        self.assertEquals(digitDegree(91), 2)




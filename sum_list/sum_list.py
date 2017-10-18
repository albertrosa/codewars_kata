from __future__ import division
import unittest


def sum_list(l):

    calced = []
    removed = []

    for num in l:
        if num not in calced and num not in removed:
            calced.append(num)
        else:
            if num in calced:
                calced.remove(num)
            removed.append(num)

    return sum(calced)


class TestSumList(unittest.TestCase):

    def test_sum_list(self):
        row1 = [2, 1, 1]
        row2 = [1, 1, 1]
        row3 = [1,1,2,3]
        row4 = [1,1,2,2,3]

        self.assertEquals(sum_list(row1), 2)
        self.assertEquals(sum_list(row3), 5)
        self.assertEquals(sum_list(row4), 3)




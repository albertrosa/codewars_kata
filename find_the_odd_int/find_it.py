import unittest


def find_it(seq):
    odd = None

    for number in seq:
        if seq.count(number) % 2 > 0:
            odd = number
            break

    return odd


class TestFindIt(unittest.TestCase):

    def test_find_it(self):
        self.assertEqual(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)

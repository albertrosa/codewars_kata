import unittest


def find_longest(arr):
    arr.sort()
    arr.reverse()
    return arr[0]


class TestFindLongest(unittest.TestCase):

    def test_findLongest(self):
        self.assertEqual(find_longest([1, 10, 100]), 100)
        self.assertEqual(find_longest([9000, 8, 800]), 9000)
        self.assertEqual(find_longest([8, 900, 500]), 900)
        self.assertEqual(find_longest([3, 40000, 100]), 40000)
        self.assertEqual(find_longest([1, 200, 100000]), 100000)

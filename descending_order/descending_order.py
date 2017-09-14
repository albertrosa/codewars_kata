import unittest


def Descending_Order(num):
    # Bust a move right here
    num_list = list(str(num))
    num_list.sort()
    num_list.reverse()
    return int("".join(num_list))


class TestDecendingOrder(unittest.TestCase):

    def test_decending_order(self):
        self.assertEqual(Descending_Order(0), 0)
        self.assertEqual(Descending_Order(15), 51)
        self.assertEqual(Descending_Order(123456789), 987654321)

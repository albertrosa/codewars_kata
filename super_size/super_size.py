import unittest


def super_size(n):

    def _get_largest(list):
        largest = 0
        cnt = 0
        while cnt < list.__len__():
            if int(list[cnt]) > largest:
                new_largest = int(list[cnt])
                list[cnt] = str(largest)
                largest = new_largest
            cnt += 1

        return largest, list

    numbers = list(str(n))
    final_number = []
    new_list = numbers

    while final_number.__len__() < numbers.__len__():
        next_number, new_list = _get_largest(new_list)
        final_number.append(str(next_number))

    return int("".join(final_number))


class TestSuperSize(unittest.TestCase):

    def test_super_size(self):
        self.assertEqual(super_size(69), 96)
        self.assertEqual(super_size(513), 531)
        self.assertEqual(super_size(2017), 7210)
        self.assertEqual(super_size(414), 441)
        self.assertEqual(super_size(608719), 987610)
        self.assertEqual(super_size(123456789), 987654321)
        self.assertEqual(super_size(700000000001), 710000000000)
        self.assertEqual(super_size(666666), 666666)
        self.assertEqual(super_size(2), 2)
        self.assertEqual(super_size(0), 0)




import unittest


def insert_dash(num):
    nums = list(str(num))

    final_num = []
    cnt = 0
    while cnt < len(nums):
        final_num.append(nums[cnt])

        if int(nums[cnt]) & 1:
            if cnt + 1 < len(nums) and int(nums[cnt + 1]) & 1:
                final_num.append('-')
        cnt += 1

    return "".join(final_num)


class TestInsertDash(unittest.TestCase):

    def test_insertDash(self):
        self.assertEqual(insert_dash(454793), '4547-9-3')
        self.assertEqual(insert_dash(123456), '123456')
        self.assertEqual(insert_dash(1003567), '1003-567')
        self.assertEqual(insert_dash(24680), '24680')
        self.assertEqual(insert_dash(13579), '1-3-5-7-9')

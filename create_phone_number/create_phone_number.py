import unittest


def create_phone_number(n):
    special = ['(', ') ', '-']

    final = []
    cnt = 0
    while cnt < n.__len__() + special.__len__():
        if cnt == 0:
            final.append(special[cnt])
        if cnt == 3:
            final.append(special[1])
        if cnt == 6:
            final.append(special[2])

        if cnt < n.__len__():
            final.append(str(n[cnt]))

        cnt += 1

    return ''.join(final)


class TestCreatePhoneNumber(unittest.TestCase):

    def test_create_phone_number(self):
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        self.assertEqual(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        self.assertEqual(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
        self.assertEqual(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")

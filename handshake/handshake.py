import unittest
import math


def get_participants(handshakes):
    result = int(1 + math.sqrt((1 + 4) * (2 * handshakes))) / 2

    if int(1 + math.sqrt((1 + 4) * (2 * handshakes))) % 2:
         result = int(result) + 1

    return int(result)


class TestGetParticipants(unittest.TestCase):

    def test_get_participants(self):
        self.assertEqual(get_participants(0), 1)
        self.assertEqual(get_participants(1), 2)
        self.assertEqual(get_participants(3), 3)
        self.assertEqual(get_participants(6), 4)
        self.assertEqual(get_participants(7), 5)

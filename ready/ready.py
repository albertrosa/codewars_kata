import unittest


def cannons_ready(gunners):
    for i in gunners:
        if gunners[i] != 'aye':
            return 'Shiver me timbers!'
    return 'Fire!'


class TestCannonReady(unittest.TestCase):

    def test_cannon(self):
        a = {'Mike': 'aye', 'Joe': 'aye', 'Johnson': 'aye', 'Peter': 'aye'}
        b = {'Mike': 'aye', 'Joe': 'nay', 'Johnson': 'aye', 'Peter': 'aye'}
        self.assertEquals(cannons_ready(a), 'Fire!')
        self.assertEquals(cannons_ready(b), 'Shiver me timbers!')
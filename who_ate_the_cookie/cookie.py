import unittest


def cookie(x):
    base = "Who ate the last cookie? It was %s!"
    if type(x) is str:
        return base % 'Zach'
    elif type(x) in [int, float]:
        return base % 'Monica'
    else:
        return base % 'the dog'


class TestCookie(unittest.TestCase):

    def test_cookie(self):
        self.assertEquals(cookie("Ryan"), "Who ate the last cookie? It was Zach!")
        self.assertEquals(cookie(2.3), "Who ate the last cookie? It was Monica!")
        self.assertEquals(cookie(26), "Who ate the last cookie? It was Monica!")
        self.assertEquals(cookie(True), "Who ate the last cookie? It was the dog!")
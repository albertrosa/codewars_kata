import unittest


def solution(string):
    letters = list(string)
    letters.reverse()
    return "".join(letters)


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution('world'), 'dlrow')
        self.assertEqual(solution('hello'), 'olleh')
        self.assertEqual(solution(''), '')
        self.assertEqual(solution('h'), 'h')

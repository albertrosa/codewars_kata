import unittest


def solution(number):

    numbers = []

    cnt = 1
    while number - cnt > 0:
        check = number - cnt
        if check % 3 == 0 or (number - cnt) % 5 == 0:
            if check not in numbers:
                numbers.append(check)
        cnt += 1

    fin = 0

    for num in numbers:
        fin += num
    return fin


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(10), 23)

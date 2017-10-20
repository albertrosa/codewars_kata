from __future__ import division
import unittest


def goodVsEvil(good, evil):
    # Hobbits, Men, Elves, Dwarves, Eagles, Wizards.
    good_worth = [1, 2, 3, 3, 4, 10]
    # Orcs, Men, Wargs, Goblins, Uruk Hai, Trolls, Wizards.
    evil_worth = [1, 2, 2, 2, 3, 5, 10]

    good_power = 0
    evil_power = 0
    good_count = good.split()
    evil_count = evil.split()
    count = 0

    while count < good_worth.__len__():
        good_power += int(good_count[count]) * good_worth[count]
        count += 1

    count = 0

    while count < evil_worth.__len__():
        evil_power += int(evil_count[count]) * evil_worth[count]
        count += 1

    if evil_power < good_power:
        return "Battle Result: Good triumphs over Evil"
    elif good_power < evil_power:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"


class TestGoodVsEvil(unittest.TestCase):

    def test_good_vs_evil(self):
        self.assertEquals(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'), 'Battle Result: Evil eradicates all trace of Good', 'Evil should win')
        self.assertEquals(goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0'), 'Battle Result: Good triumphs over Evil',
                           'Good should win')
        self.assertEquals(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'), 'Battle Result: No victor on this battle field',
                           'Should be a tie')




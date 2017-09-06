from __future__ import division
import unittest


def bmi(weight, height):
    bmi = weight / (height * height)

    if bmi <= 18.5:
        return "Underweight"
    if bmi <= 25.0:
        return "Normal"
    if bmi <= 30.0:
        return "Overweight"
    if bmi > 30:
        return "Obese"


class TestBMI(unittest.TestCase):

    def test_bmi(self):
        self.assertEqual(bmi(50, 1.80), "Underweight")
        self.assertEqual(bmi(80, 1.80), "Normal")
        self.assertEqual(bmi(90, 1.80), "Overweight")
        self.assertEqual(bmi(110, 1.80), "Obese")
        self.assertEqual(bmi(50, 1.50), "Normal")
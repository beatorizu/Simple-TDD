from unittest import TestCase
from calculator import Calculator


class SumNumTest(TestCase):

    def setUp(self):
        self.valueA = 1
        self.valueB = 2
        self.calc = Calculator()

    def test_can_sum_numbers(self):
        sum_ = self.calc.sum(self.valueA, self.valueB)
        self.assertEqual(3, sum_)


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


class SubNumTest(TestCase):

    def setUp(self):
        self.valueA = 1
        self.valueB = 2
        self.calc = Calculator()

    def test_can_sub_numbers(self):
        sub_ = self.calc.sub(self.valueA, self.valueB)
        self.assertEqual(-1, sub_)


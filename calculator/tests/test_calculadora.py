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


class DivNumTest(TestCase):

    def setUp(self):
        self.valueA = 6
        self.valueB = 2
        self.valueC = 0
        self.calc = Calculator()

    def test_can_div_numbers(self):
        div_ = self.calc.div(self.valueA, self.valueB)
        self.assertEqual(3, div_)

    def test_can_div_number_by_zero(self):
        self.assertRaises(ZeroDivisionError,
                          lambda: self.calc.div(self.valueA, self.valueC))

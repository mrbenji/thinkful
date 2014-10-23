import unittest

from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
    def test_zero_discounts(self):
        self.assertTrue(200,calculate_discount(200, 0, 0))

    def test_zero_relative_discount(self):
        self.assertTrue(190,calculate_discount(100, 0, 10))

    def test_zero_absolute_discount(self):
        self.assertTrue(100,calculate_discount(200, 50, 0))

if __name__ == "__main__":
    unittest.main()
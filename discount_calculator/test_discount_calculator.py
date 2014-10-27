import unittest

from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
    def test_zero_discounts(self):
        self.assertEqual(200, calculate_discount(200, 0, 0))

    def test_zero_relative_discount(self):
        self.assertEqual(90, calculate_discount(100, 0, 10))

    def test_zero_absolute_discount(self):
        self.assertEqual(100, calculate_discount(200, 50, 0))

    def test_mixed_discounts(self):
        self.assertEqual(140, calculate_discount(200, 25, 10))
        self.assertEqual(119.75, calculate_discount(195.44, 33.33, 10.55))

    # Assume we never want to pay a customer to take merchandise
    def test_discount_greater_than_cost(self):
        self.assertEqual(0, calculate_discount(212.50, 150, 0))
        self.assertEqual(0, calculate_discount(5, 0, 10))

    # Assume if discount is negative, customer will decline it.
    def test_negative_discount(self):
        self.assertEqual(200, calculate_discount(200, -25, 0))
        self.assertEqual(17.99, calculate_discount(17.99, 0, -20))

    def test_negative_cost(self):
        self.assertEqual(0, calculate_discount(-10, 10, 5))

if __name__ == "__main__":
    unittest.main()
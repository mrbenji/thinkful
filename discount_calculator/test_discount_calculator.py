import unittest

from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
    def test_zero_discounts(self):
        self.assertEqual("200.00",calculate_discount(200, 0, 0))

    def test_zero_relative_discount(self):
        self.assertEqual("90.00",calculate_discount(100, 0, 10))

    def test_zero_absolute_discount(self):
        self.assertEqual("100.00",calculate_discount(200, 50, 0))

    def test_mixed_discounts(self):
        self.assertTrue("140.00", calculate_discount(200, 25, 10))
        self.assertEqual("119.75", calculate_discount(195.44, 33.33, 10.55))

    # Going to assume we never want to pay a customer to take merchandise
    def test_discount_greater_than_cost(self):
        self.assertEqual("0.00", calculate_discount(212.50, 150, 0))
        self.assertEqual("0.00", calculate_discount(5, 0, 10))

if __name__ == "__main__":
    unittest.main()
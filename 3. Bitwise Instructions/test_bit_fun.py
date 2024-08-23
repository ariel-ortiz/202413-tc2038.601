import unittest
from bit_fun import is_even, is_power_of_2, int_mul

class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-2))

    def test_odd_number(self):
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))
        self.assertFalse(is_even(-3))

    def test_positive_powers_of_2(self):
        self.assertTrue(is_power_of_2(1))
        self.assertTrue(is_power_of_2(2))
        self.assertTrue(is_power_of_2(4))
        self.assertTrue(is_power_of_2(8))
        self.assertTrue(is_power_of_2(16))
        self.assertTrue(is_power_of_2(1024))

    def test_non_powers_of_2(self):
        self.assertFalse(is_power_of_2(0))
        self.assertFalse(is_power_of_2(3))
        self.assertFalse(is_power_of_2(5))
        self.assertFalse(is_power_of_2(6))
        self.assertFalse(is_power_of_2(7))
        self.assertFalse(is_power_of_2(9))
        self.assertFalse(is_power_of_2(1023))

    def test_negative_numbers(self):
        self.assertFalse(is_power_of_2(-1))
        self.assertFalse(is_power_of_2(-2))
        self.assertFalse(is_power_of_2(-4))
        self.assertFalse(is_power_of_2(-8))

    def test_positive_numbers_int_mul(self):
        self.assertEqual(int_mul(3, 4), 12)
        self.assertEqual(int_mul(7, 5), 35)
        self.assertEqual(int_mul(666, 12345), 8221770)

    def test_negative_numbers_int_mul(self):
        self.assertEqual(int_mul(-3, -4), 12)
        self.assertEqual(int_mul(-7, -5), 35)
        self.assertEqual(int_mul(-666, -12345), 8221770)

    def test_mixed_sign_numbers_int_mul(self):
        self.assertEqual(int_mul(-3, 4), -12)
        self.assertEqual(int_mul(7, -5), -35)
        self.assertEqual(int_mul(-666, 12345), -8221770)
        self.assertEqual(int_mul(666, -12345), -8221770)

    def test_zero_int_mul(self):
        self.assertEqual(int_mul(0, 4), 0)
        self.assertEqual(int_mul(7, 0), 0)
        self.assertEqual(int_mul(0, 0), 0)
        self.assertEqual(int_mul(666, 0), 0)

if __name__ == '__main__':
    unittest.main()

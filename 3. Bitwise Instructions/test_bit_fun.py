import unittest
from bit_fun import is_even, is_power_of_2, int_mul, bin_with_num_bits

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

    def test_positive_numbers_bin_with_num_bits(self):
        self.assertEqual(bin_with_num_bits(5, 4), '0101')
        self.assertEqual(bin_with_num_bits(3, 3), '011')
        self.assertEqual(bin_with_num_bits(8, 4), '1000')

    def test_negative_numbers_bin_with_num_bits(self):
        self.assertEqual(bin_with_num_bits(-1, 4), '1111')
        self.assertEqual(bin_with_num_bits(-3, 4), '1101')
        self.assertEqual(bin_with_num_bits(-5, 16), '1111111111111011')

    def test_zero_bin_with_num_bits(self):
        self.assertEqual(bin_with_num_bits(0, 4), '0000')
        self.assertEqual(bin_with_num_bits(0, 1), '0')

    def test_max_min_values_bin_with_num_bits(self):
        self.assertEqual(bin_with_num_bits(7, 4), '0111')
        self.assertEqual(bin_with_num_bits(-8, 4), '1000')

    def test_value_error_bin_with_num_bits(self):
        with self.assertRaises(ValueError):
            bin_with_num_bits(16, 4)
        with self.assertRaises(ValueError):
            bin_with_num_bits(-9, 4)
        with self.assertRaises(ValueError):
            bin_with_num_bits(1, 0)

if __name__ == '__main__':
    unittest.main()

import unittest
from euclidean import gcd

class TestGCD(unittest.TestCase):
    def test_gcd_normal_cases(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(101, 10), 1)

    def test_gcd_with_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)

    def test_gcd_both_zero(self):
        with self.assertRaises(ValueError):
            gcd(0, 0)

    def test_gcd_negative_values(self):
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(48, -18), 6)
        self.assertEqual(gcd(-48, -18), 6)
        self.assertEqual(gcd(-101, 10), 1)
        self.assertEqual(gcd(101, -10), 1)
        self.assertEqual(gcd(-101, -10), 1)

if __name__ == '__main__':
    unittest.main()

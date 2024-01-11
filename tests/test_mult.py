import unittest
from calculatrice import multiplier

class TestMultiplication(unittest.TestCase):

    def test_multiplication_positives(self):
        self.assertEqual(multiplier(5, 3), 15)

    def test_multiplication_negatives(self):
        self.assertEqual(multiplier(-5, -3), 15)

    def test_multiplication_melange(self):
        self.assertEqual(multiplier(4, -2), -8)

if __name__ == '__main__':
    unittest.main()

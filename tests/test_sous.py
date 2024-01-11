import unittest
from calculatrice import soustraire

class TestSubtraction(unittest.TestCase):

    def test_subtraction_positives(self):
        self.assertEqual(soustraire(10, 2), 8)

    def test_subtraction_negatives(self):
        self.assertEqual(soustraire(-10, -2), -8)

    def test_subtraction_melange(self):
        self.assertEqual(soustraire(5, -3), 8)

if __name__ == '__main__':
    unittest.main()

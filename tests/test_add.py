import unittest
from calculatrice import additionner

class TestAddition(unittest.TestCase):

    def test_addition_positives(self):
        self.assertEqual(additionner(3, 5), 8)

    def test_addition_negatives(self):
        self.assertEqual(additionner(-3, -5), -8)

    def test_addition_melangee(self):
        self.assertEqual(additionner(2, -7), -5)

if __name__ == '__main__':
    unittest.main()

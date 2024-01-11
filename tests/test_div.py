import unittest
from calculatrice import diviser

class TestDivision(unittest.TestCase):

    def test_division_positives(self):
        self.assertEqual(diviser(10, 2), 5)

    def test_division_negatives(self):
        self.assertEqual(diviser(-10, -2), 5)

    def test_division_par_zero(self):
        with self.assertRaises(ZeroDivisionError):
            diviser(5, 0)

if __name__ == '__main__':
    unittest.main()

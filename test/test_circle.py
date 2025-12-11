import unittest
from geometric_lib.circle import area, perimeter
import math

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test_zero(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

if __name__ == "__main__":
    unittest.main()

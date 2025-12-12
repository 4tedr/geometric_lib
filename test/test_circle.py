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

    def test_string_input(self):
        with self.assertRaises(TypeError):
            area("5")
        with self.assertRaises(TypeError):
            area("hello")
        with self.assertRaises(TypeError):
            area("3.14")
        with self.assertRaises(TypeError):
            perimeter("10")
        with self.assertRaises(TypeError):
            perimeter("radius")

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            area(-1)
        with self.assertRaises(ValueError):
            perimeter(-1)

if __name__ == "__main__":
    unittest.main()
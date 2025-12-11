import unittest
from geometric_lib.triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_area_34(self):
        self.assertAlmostEqual(area(3, 4), 6)

if __name__ == "__main__":
    unittest.main()

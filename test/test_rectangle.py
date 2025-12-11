import unittest
from geometric_lib.rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_usual(self):
        self.assertEqual(area(5, 10), 50)

    def test_perimeter_usual(self):
        self.assertEqual(perimeter(5, 10), 30)

    def test_zero_side(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(perimeter(0, 10), 20)

if __name__ == "__main__":
    unittest.main()

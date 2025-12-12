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

    def test_string_input(self):
        with self.assertRaises(TypeError):
            area("5", 10)
        with self.assertRaises(TypeError):
            area(5, "10")
        with self.assertRaises(TypeError):
            perimeter("7", 3)
        with self.assertRaises(TypeError):
            perimeter(7, "3")

    def test_negative_values(self):
        self.assertEqual(area(-5, 10), -50) 
        self.assertEqual(perimeter(-5, 10), 10)


if __name__ == "__main__":
    unittest.main()
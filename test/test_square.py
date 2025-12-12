import unittest
from geometric_lib.square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 25)

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 20)

    def test_zero(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            area("5")
        with self.assertRaises(TypeError):
            area("hello")
        with self.assertRaises(TypeError):
            perimeter("10")
        with self.assertRaises(TypeError):
            perimeter("side")

    def test_negative_values(self):
        self.assertEqual(area(-5), 25) 
        self.assertEqual(perimeter(-5), -20) 
        

if __name__ == "__main__":
    unittest.main()
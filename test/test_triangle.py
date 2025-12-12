import unittest
from geometric_lib.triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_area_34(self):
        self.assertAlmostEqual(area(3, 4), 6)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            area("3", 4)
        with self.assertRaises(TypeError):
            area(3, "4")
        with self.assertRaises(TypeError):
            area("height", "base")
        
        with self.assertRaises(TypeError):
            perimeter("3", 4, 5)
        with self.assertRaises(TypeError):
            perimeter(3, "4", 5)
        with self.assertRaises(TypeError):
            perimeter(3, 4, "5")
        with self.assertRaises(TypeError):
            perimeter("a", "b", "c")

    def test_negative_values(self):
        self.assertEqual(area(-3, 4), -6)  
        self.assertEqual(area(3, -4), -6)  
        
        self.assertEqual(perimeter(-3, 4, 5), 6) 
        self.assertEqual(perimeter(3, -4, 5), 4)  
        self.assertEqual(perimeter(3, 4, -5), 2)  

if __name__ == "__main__":
    unittest.main()
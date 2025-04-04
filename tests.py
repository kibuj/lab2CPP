import unittest
from main import *

class TestShapes(unittest.TestCase):

    def test_get_rectangle_type(self):
        self.assertEqual(get_rectangle_type(5, 5), "Квадрат")
        self.assertEqual(get_rectangle_type(5, 10), "Прямокутник")

    def test_get_triangle_type(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "Рівносторонній трикутник")
        self.assertEqual(get_triangle_type(3, 3, 4), "Рівнобедрений трикутник")
        self.assertEqual(get_triangle_type(3, 4, 5), "Прямокутний трикутник")
        self.assertEqual(get_triangle_type(4, 5, 6), "Звичайний трикутник")

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 10), 50)
        self.assertEqual(rectangle_area(3, 7), 21)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)
        self.assertEqual(rectangle_perimeter(3, 7), 20)

    def test_triangle_area(self):
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.0)
        self.assertAlmostEqual(triangle_area(5, 12, 13), 30.0)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(5, 12, 13), 30)

if __name__ == "__main__":
    unittest.main()

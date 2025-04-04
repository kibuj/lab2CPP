import unittest
from lab4 import *


class TestShapes(unittest.TestCase):

    def test_get_rectangle_type(self):
        self.assertEqual(Rectangle(5, 5).get_type(), "Квадрат")
        self.assertEqual(Rectangle(5, 10).get_type(), "Прямокутник")

    def test_rectangle_area(self):
        self.assertEqual(Rectangle(5, 10).area(), 50)
        self.assertEqual(Rectangle(3, 7).area(), 21)

    def test_rectangle_perimeter(self):
        self.assertEqual(Rectangle(5, 10).perimeter(), 30)
        self.assertEqual(Rectangle(3, 7).perimeter(), 20)

    def test_get_triangle_type(self):
        self.assertEqual(Triangle(3, 3, 3).get_type(), "Рівносторонній трикутник")
        self.assertEqual(Triangle(3, 3, 4).get_type(), "Рівнобедрений трикутник")
        self.assertEqual(Triangle(3, 4, 5).get_type(), "Прямокутний трикутник")
        self.assertEqual(Triangle(4, 5, 6).get_type(), "Звичайний трикутник")

    def test_triangle_area(self):
        self.assertAlmostEqual(Triangle(3, 4, 5).area(), 6.0)
        self.assertAlmostEqual(Triangle(5, 12, 13).area(), 30.0)

    def test_triangle_perimeter(self):
        self.assertEqual(Triangle(3, 4, 5).perimeter(), 12)
        self.assertEqual(Triangle(5, 12, 13).perimeter(), 30)

    def test_shape_factory(self):
        rect = ShapeFactory.create_shape(["прямокутник", "5", "10"])
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.area(), 50)
        self.assertEqual(rect.perimeter(), 30)

        tri = ShapeFactory.create_shape(["трикутник", "3", "4", "5"])
        self.assertIsInstance(tri, Triangle)
        self.assertAlmostEqual(tri.area(), 6.0)
        self.assertEqual(tri.perimeter(), 12)

        invalid_shape = ShapeFactory.create_shape(["трикутник", "1", "1", "3"])
        self.assertIsNone(invalid_shape)

    def test_sphere_area(self):
        sphere = Sphere(3)
        self.assertAlmostEqual(sphere.area(), 4 * math.pi * 3 ** 2)

    def test_sphere_perimeter(self):
        sphere = Sphere(3)
        self.assertAlmostEqual(sphere.perimeter(), 2 * math.pi * 3)

    def test_sphere_volume(self):
        sphere = Sphere(3)
        self.assertAlmostEqual(sphere.volume(), (4 / 3) * math.pi * 3 ** 3)

    def test_cuboid_area(self):
        cuboid = Cuboid(2, 4, 6)
        self.assertEqual(cuboid.area(), 2 * (2 * 4 + 2 * 6 + 4 * 6))

    def test_cuboid_perimeter(self):
        cuboid = Cuboid(2, 4, 6)
        self.assertEqual(cuboid.perimeter(), 4 * (2 + 4 + 6))

    def test_cuboid_volume(self):
        cuboid = Cuboid(2, 4, 6)
        self.assertEqual(cuboid.volume(), 2 * 4 * 6)


if __name__ == "__main__":
    unittest.main()

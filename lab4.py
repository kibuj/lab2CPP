import csv
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    def __str__(self):
        return (f"{self.get_type()}:\n"
                f"  Площа: {self.area():.2f}\n"
                f"  Периметр: {self.perimeter():.2f}\n"
                + "-" * 30)


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def get_type(self):
        return "Квадрат" if self.length == self.width else "Прямокутник"


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a, self.b, self.c = sorted([a, b, c])

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def get_type(self):
        if self.a == self.b == self.c:
            return "Рівносторонній трикутник"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Рівнобедрений трикутник"
        elif math.isclose(self.a**2 + self.b**2, self.c**2, rel_tol=1e-9):
            return "Прямокутний трикутник"
        else:
            return "Звичайний трикутник"


class Cuboid(Shape):
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    def area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    def perimeter(self):
        return 4 * (self.length + self.width + self.height)

    def get_type(self):
        return "Прямокутний паралелепіпед"

    def volume(self):
        return self.length * self.width * self.height


class Sphere(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 4 * math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def get_type(self):
        return "Сфера"

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3


class ShapeFactory:
    @staticmethod
    def create_shape(data):
        shape_type = data[0].lower()
        try:
            if shape_type == "прямокутник":
                length, width = map(float, data[1:3])
                if length > 0 and width > 0:
                    return Rectangle(length, width)
            elif shape_type == "трикутник":
                a, b, c = map(float, data[1:4])
                if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
                    return Triangle(a, b, c)
            elif shape_type == "паралелепіпед":
                length, width, height = map(float, data[1:4])
                if length > 0 and width > 0 and height > 0:
                    return Cuboid(length, width, height)
            elif shape_type == "сфера":
                radius = float(data[1])
                if radius > 0:
                    return Sphere(radius)
        except ValueError:
            return None
        return None

def process_shapes_from_csv(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            shape = ShapeFactory.create_shape(row)
            if shape:
                print(shape)


process_shapes_from_csv('CSVfile.csv')

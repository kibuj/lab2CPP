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




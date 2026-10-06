from math import pi
from domain.shape import Shape

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

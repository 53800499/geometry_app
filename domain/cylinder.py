from math import pi
from domain.solid import Solid

class Cylinder(Solid):
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def volume(self):
        return pi * self.radius ** 2 * self.height

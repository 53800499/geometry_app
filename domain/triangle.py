from domain.shape import Shape

class Triangle(Shape):
    def __init__(self, base: float, height: float):
       self.base = base
       self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base + self.height + (self.base**2 + self.height**2)**0.5 
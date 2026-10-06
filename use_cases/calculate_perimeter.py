from domain.shape import Shape

class CalculatePerimeter:
    def execute(self, shape: Shape) -> float:
        return shape.perimeter()

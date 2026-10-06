from domain.solid import Solid

class CalculateVolume:
    def execute(self, solid: Solid) -> float:
        return solid.volume()

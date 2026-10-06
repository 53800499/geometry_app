from domain.solid import Solid

class Cube(Solid):
    def __init__(self, side: float):
        self.side = side

    def volume(self):
        return self.side ** 3

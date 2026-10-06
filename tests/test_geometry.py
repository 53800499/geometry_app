from domain.circle import Circle
from domain.cube import Cube
from use_cases.calculate_area import CalculateArea
from use_cases.calculate_volume import CalculateVolume

def test_circle_area():
    c = Circle(2)
    area = CalculateArea().execute(c)
    assert round(area, 2) == 12.57  # πr²

def test_cube_volume():
    cube = Cube(3)
    v = CalculateVolume().execute(cube)
    assert v == 27

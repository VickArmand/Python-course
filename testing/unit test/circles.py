from math import pi
def circle_area(radius):
    # if type(radius) not in [int, float]:
    #     raise TypeError("Invalid type")
    if radius < 0:
        raise ValueError("Invalid Type")
    return pi * (radius ** 2)
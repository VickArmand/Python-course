import unittest
from circles import circle_area
from math import pi
class test_circles(unittest.TestCase):
    def testArea(self):
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(2),pi*4)
    def testRadius(self):
        self.assertRaises(ValueError, circle_area, -1)
    def testValueType(self):
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "string")

    # to run this tests first navigate this folder
    # run python -m unittest test_circles.py
    # to show verbose
    # use python -m unittest test_circles.py -v
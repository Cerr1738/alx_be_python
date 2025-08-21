
import math

class Shape:
    def area(self):
        """Base method to calculate area, expected to be overridden."""
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle: length × width"""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate area of a circle: π × r²"""
        return math.pi * (self.radius ** 2)

# polymorphism_demo.py
# Demonstrates polymorphism via method overriding:
# - Shape defines the interface (area)
# - Rectangle and Circle override area() with their own formulas

import math

class Shape:
    """Base class that defines the interface: area() must be implemented by subclasses."""
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def square(self):
        pass

    def __repr__(self):
        return f"{self.name}: {self.square()}"

class Circle(Shape):
    name = 'Circle'
    def __init__(self, r):
        self.r = r
    def square(self):
        return math.pi * self.r ** 2

class Rectangle(Shape):
    name = 'Rectangle'
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def square(self):
        return self.a * self.b

class Triangle(Shape):
    name = 'Triangle'
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def square(self):
        return 0.5 * self.base * self.height


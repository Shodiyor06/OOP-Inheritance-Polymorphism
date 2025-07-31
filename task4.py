import math

class Shape:
    def area(self):
        pass 
# radius
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# eni va bo‘yi
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# asos va balandlik
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

print(f"Aylana yuzi: {circle.area():.2f}")
print(f"Togri tortburchak yuzi: {rectangle.area()}")
print(f"Uchburchak yuzi: {triangle.area()}")

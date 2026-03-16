# Bài 8:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"
v1 = Vector(5, 2)
v2 = Vector(3, 7)
v3 = v1 + v2
print(f" Vector 1:{v1}")
print(f" Vector 2:{v2}")
print(f" Vector 3:{v3}")


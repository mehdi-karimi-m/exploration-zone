from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

point1 = Point(x=1, y=3)
point2 = Point(x=10, y=20)
point3 = Point(x=1, y=3)
print(point1.x)
print(point1 == point2)
print(point1 == point3)

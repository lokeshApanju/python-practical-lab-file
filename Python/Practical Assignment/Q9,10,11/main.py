from shapes.circle import Circle, Point
from shapes.rectangle import Rectangle

p = Point(1, 3)
c = Circle(p, 6)
r = Rectangle(4, 7)

print(f"Circle area = {c.area()}")
print(f"Rectangle area = {r.area()}")
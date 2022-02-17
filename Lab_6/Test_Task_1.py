from Task_1 import *

def TestPointLocation():
    point = Point(3,4)
    center = Point(0,0)
    circle = Circle(center,5)
    assert circle.pointLocation(point) == "On Circle"
    circle.radius = 6
    assert circle.pointLocation(point) == "In Circle"
    circle.radius = 2
    assert circle.pointLocation(point) == "Outside Circle"
    
TestPointLocation()
print("Pass")
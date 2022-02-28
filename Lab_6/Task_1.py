from math import sqrt

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def distance(self,other):
        return(sqrt((other.x - self.x)**2+(other.y - self.y)**2))

class Circle:
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius
        
    def pointLocation(self,point):
        distanceToCenter = self.center.distance(point)
        if distanceToCenter == self.radius:
            return "On Circle"
        elif distanceToCenter < self.radius:
            return "In Circle"
        else:
            return "Outside Circle"
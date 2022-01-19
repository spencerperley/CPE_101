from math import sqrt
x1 = int(input("enter the first point x value: "))
y1 = int(input("enter the first point y value: "))

x2 = int(input("enter the second point x value: "))
y2 = int(input("enter the second point y value: "))


print(f"The distance between the points is {(((x2-x1)**2)+((y2-y1)**2))**(1/2)}")
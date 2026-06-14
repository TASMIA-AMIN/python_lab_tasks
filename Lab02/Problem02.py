import math

x1 = int(input("1st point x value: "))
y1 = int(input("1st point y value: "))
x2 = int(input("2nd point x value: "))
y2 = int(input("2nd point y value: "))

dist = math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))

print("Distance between two points:", dist)
'''
Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
'''
#importing math module 
import math
#declaring the point p1 and p2
p1 = [4, 0]
p2 = [6, 6]
#distance for caluclating distance between two points.
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
print(distance)

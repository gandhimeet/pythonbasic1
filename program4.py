'''
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''
#importing math and constant pi 
from math import pi
# r variable for storing radius in float
r = float(input("Ente the Radius of the circle:"))
#applying area of circle formula in print using concatenation
print("The area of circle with radius" + str(r) + "is:" + str(pi*r**2))
#* for multiplucation 
#** for square 
#pi ~ 3.17

'''
Write a Python program to get the volume of a sphere with radius six.
'''
# volume of sphere is 4/3 pi r^3
#importing the pi from math module 
from math import pi
#r variable for storing the radius of sphere 
r = 6.0
#voume of sphere 
volume = 4.0/3.0*pi*r**3
print("The Volume of sphere with radius" + str(r) + "is:" + str(volume))
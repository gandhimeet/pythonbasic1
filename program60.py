'''
Write a Python program to calculate the hypotenuse of a right angled triangle.
'''
#importing sqrt from math
from math import sqrt
#displaying the message to input the shorter sides of triangle
print("Input lengths of shorter triangle sides:")
#input of side a
a = float(input("a: "))
#input of side b
b = float(input("b: "))
#calculating hypotenuse of a right angled triangle
c = sqrt(a**2 + b**2)
#displaying the hypotenuse 
print("The length of the hypotenuse is:", c )

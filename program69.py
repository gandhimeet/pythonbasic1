'''
Write a Python program 
to sort three integers without using conditional statements and loops.
'''
#input of x y z first second and third number respectively 
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))
#output 
a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)

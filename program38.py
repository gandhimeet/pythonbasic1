'''
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
'''
#x and y for storing value 
x = int(input("Enter the value of X:"))
y = int(input("Enter the value of Y:"))
#result for storing result of expression
result = x*x+2*x*y+y*y
#printing result through format method
print("({} + {}) ^ 2) = {}".format(x,y,result))
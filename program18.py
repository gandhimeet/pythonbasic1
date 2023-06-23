'''
Write a Python program to calculate the sum of three given numbers. 
If the values are equal, return three times their sum.
'''
#sum_thrice function name
#x for x variable 1st
#y for y variable 2nd
#z for z variable 3rd
def sum_thrice(x,y,z):    
    sum = x + y + z
    if x==y==z:
        sum = sum*3
    return sum
#x y z are different
print(sum_thrice(1,2,3))
#x y z are equal 
print(sum_thrice(3,3,3))
'''
Write a Python program to sum three given integers. 
However, if two values are equal, the sum will be zero.
'''
#function name sum_three having parameter x,y,z
def sum_three(x, y, z):
    #checking x,y,z are same or not
    if x == y or y == z or x==z:
        #hence sum = 0
        sum = 0
    else:
        #calculating sum as usal
        sum = x + y + z
    #return sum 
    return sum
#calling function sum_three 
print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))

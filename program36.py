'''
Write a Python program to add two objects if both objects are integers.
'''
#add function with parameter x and y 
def add(x,y):
    #checks x and y is object and integer
    if not (isinstance(x,int) and isinstance(y,int)):
        #return must be integers
        return "Inputs must be Integers."
    #return sum of x and y
    return x+y

#calling function with different parameters
print(add(1,2))
print(add('a',2))
print(add(3,'b'))
print(add('a','b'))
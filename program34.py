'''
Write a Python program to sum two given integers. 
However, if the sum is between 15 and 20 it will return 20.
'''
#function sum having parameter x and y 
def sum(x,y):
    #sum of x and y 
    sum = x+y
    #checking the sum is between 15 and 20
    if sum in range(15,20):
        #return 20
        return 20
    else:
        #return sum
        return sum 

#calling sum function with different parameters
print(sum(5,10))
print(sum(10,20))
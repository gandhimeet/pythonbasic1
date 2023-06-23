'''
Write a Python program to calculate the difference between a given number and 17. 
If the number is greater than 17, return twice the absolute difference.
'''
#def keyword for defining the function
#difference is the function name 
#n is parameter 
# if-else condition statement
#return keyword used for returning the value
def difference(n):
    if n <= 17:
        return 17-n 
    else:
        return(n-17)*2
#n=22 
print(difference(22))
#n=10
print(difference(10))
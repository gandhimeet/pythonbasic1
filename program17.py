'''
Write a Python program to test whether a number is within 100 of 1000 or 2000.
'''
#near_thousand is a function name which checks whether the given number near to thousand or not.
#n is variable for storing the number.
#or operator return the false or true value when the function is called.
def near_thousand(n):
    return (abs(1000-n) <= 100) or (abs(2000-n) <=100)
#calling function for check whether the number is near to the thousand 
print(near_thousand(11)) #false
print(near_thousand(22)) #false
print(near_thousand(1010)) #true
print(near_thousand(2020)) #true
print(near_thousand(4050)) #false
print(near_thousand(4500)) #false
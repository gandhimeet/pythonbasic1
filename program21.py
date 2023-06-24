'''
Write a Python program that determines whether a given number 
(accepted from the user) is even or odd, 
and prints an appropriate message to the user.
'''
#num is the integer input for number 
num = int(input("Enter a number: "))
#mod is for modulo of num 
mod = num % 2
#if else condition statement for checking odd and even
if mod > 0:
    #prints number is odd
    print("This is an odd number.")
else:
    #prints number is even
    print("This is an even number.")
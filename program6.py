'''
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''
#variable values for storing the comma separated values
values = input("Enter the Some Comma Seprated Values:")
#list variable for displaying list of values 
list = values.split(",")
print(list)
#tuple variable for displaying tuple of values
tuple = tuple(list)
print(tuple)
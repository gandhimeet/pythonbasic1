'''
Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
'''
# module calendar import 
import calendar
# y variable for storing the years 
y = int(input("Enter the Year:"))
# m variable for stroing the months
m = int(input("Enter the month:"))
#displaying the year and month based on calendar 
print(calendar.month(y,m))
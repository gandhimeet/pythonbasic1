'''
Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''
#importing the date from datetime module 
from datetime import date
#firsdate - firstdate variable for storing the firstdate.
firstdate = date(2023,6,22)
#lastdate -  lastdate variable for storing the lastdate.
lastdate =  date(2023,6,26)
#delta - delta variable for storing the difference between the firstdate and lastdate.
delta = lastdate - firstdate
#.days give days calculation based on days formatting.
print(delta.days)
'''
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2023-06-22 14:34:14
'''
# importing datetime module
import datetime

# now variable for showing date time of now()
now=datetime.datetime.now()
print("Current Date Time:")

# strftime() for formatting date time
print(now.strftime("%Y-%m-%d %H:%M:%S"))
#Y-Years
#m-months
#d-days
#H-hours
#M-minutes
#S-Seconds
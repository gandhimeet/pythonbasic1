'''
Write a Python program to convert the distance (in feet) to inches, yards, and miles.
'''
#input for ft
d_ft = int(input("Input distance in feet: "))
#ft to inches conversion equations
d_inches = d_ft * 12
#ft to yards conversion equations
d_yards = d_ft / 3.0
#ft to miles conversion equations
d_miles = d_ft / 5280.0
#displaying output
print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)

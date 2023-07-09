'''
Write a Python program to convert height (in feet and inches) to centimeters.
'''
#displaying the height
print("Input your height: ")
#input of feet 
h_ft = int(input("Feet: "))
#input of inch
h_inch = int(input("Inches: "))
#calculating height in feet and inches to centimeters
h_inch += h_ft * 12
#round off the value of centimeters
h_cm = round(h_inch * 2.54, 1)
#displaying the height in centimeters
print("Your height is : %d cm." % h_cm)

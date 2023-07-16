'''
Write a Python program to calculate the body mass index.
'''
#input of height and weight in feet and kilogram respectively
height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
#BMI as Output
print("Your body mass index is: ", round(weight / (height * height), 2))

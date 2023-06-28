'''
Write a Python program that displays your name, age, and address on three different lines.
'''
#name variable for storing name
name = str(input("Enter Your Name:"))
#age variable for storing age
age = int(input("Enter Your Age:"))
#addr variable for storing address
addr = str(input("Enter Your Address:")) 

#printing name age and address variable through formatting with format 
#replace variable at the place of {}
print("Name: {}\nAge:{}\nAddress:{}".format(name,age,addr))
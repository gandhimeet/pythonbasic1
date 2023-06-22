'''
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
'''
#filename variable for storing the name of file.
filename = input("Enter the File Name With Extension:")
#displaying the proper file name.
print("Name of File is:"+str(filename))
#extension variable for storing the extension of the file name
#split for spliting filename from "."
extension = filename.split(".")
#displaying the extension of the file name.
print ("Extension of " + str(filename) +"is:"+str(extension[-1]))
#-1 is indexing done from reverse side  
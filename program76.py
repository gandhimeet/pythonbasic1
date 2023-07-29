'''
Write a Python program to get the command-line arguments 
(name of the script, the number of arguments, arguments) passed to a script.
'''
#importing sys module 
import sys
#displaying the name of the script 
print("This is the Path/Name of Script:"),sys.argv[0]
#displaying the number of arguments
print("The Number of arguments:",len(sys.argv))
#displaying the list of arguments
print("Argument list is as follows:",str(sys.argv))

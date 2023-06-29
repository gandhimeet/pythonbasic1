'''
Write a Python program to retrieve the path and name of the file currently being executed.
'''
#importing the os module
import os 
#os.path returns path .realpath(__file__) returns current file executed
print("Name of current file:",os.path.realpath(__file__))
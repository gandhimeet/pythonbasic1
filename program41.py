'''
Write a Python program to check whether a file exists.
'''
#importing the os module having path function 
import os.path 
#os.path checks the path and is file checks the file
#returns true or false 
print(os.path.isfile('main.txt')) #main.txt is not in the directory
print(os.path.isfile('program31.py')) #program31.py is in the directory 
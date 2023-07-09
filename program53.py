'''
Write a Python program to access environment variables.
'''
#importing os module
import os
# Access all environment variables 
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable 
print(os.environ['TEMP'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')
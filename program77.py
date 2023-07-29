'''
Write a Python program to test whether the system is a big-endian platform or
a little-endian platform.
'''
#importing sys module
import sys
print()
#sys.byteorder: An indicator of the native byte order. 
#This will have the value 'big' on big-endian (most-significant byte first) platforms, 
#and 'little' on little-endian (least-significant byte first) platforms.
if sys.byteorder == 'little':
    #intel,alpha
    print('little-endian platform')
else:
    #motorola,sparc
    print('big-endian platform')
'''
Write a Python program to determine 
if a Python shell is executing in 32bit or 64bit mode on OS.
'''
#returns 32 for 32 bit and 64 for 64 bit
#importing the struct module 
import struct
#calculate the size in bit 32 or 64
print(struct.calcsize("P")*8)
'''
Write a Python program to get OS name, platform and release information.
'''
#importing the os module
import os
#importing the platform module 
import platform
#os.name gives the name of operating system
print("Name of Operating sytem:",os.name)
#platform.system() gives system name or platform
print("\nName of Platform:",platform.system())
#platform.release() gives release version of operating system
print("\nVersion of the operating system:",platform.release())
'''
Write a Python program to sort files by date.
'''
#importing libraries glob and os
import glob
import os
#files of .py extension i.e python files 
files = glob.glob("*.py")
files.sort(key=os.path.getmtime)
print("\n".join(files))
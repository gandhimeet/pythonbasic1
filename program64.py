'''
Write a Python program that retrieves the date and time of file creation and modification.
'''
#importing os module 
import os.path, time
#displaying last modified time of file 
print("Last modified: %s" % time.ctime(os.path.getmtime("program1.py")))
#displaying created time of file 
print("Created: %s" % time.ctime(os.path.getctime("program1.py")))

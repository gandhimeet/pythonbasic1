'''
Write a Python program to get an absolute file path.
'''
#function for absolute file path 
def absolute_file_path(path_fname):
        import os
        return os.path.abspath('path_fname')
#displaying output 
print("Absolute file path: ",absolute_file_path("program1.py"))

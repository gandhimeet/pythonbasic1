"""
Write a Python program to list the home directory without an absolute path.
"""
import os.path
print(os.path.expanduser('~'))

'''
Write a Python program to determine the profiling of Python programs.
Note: A profile is a set of statistics that describes how often and 
for how long various parts of the program executed. 
These statistics can be formatted into reports via the pstats module.
'''
#importing cProfile 
import cProfile
#sum function 
def sum():
    print(1+2)
#printing eacch and every details of program51.py
cProfile.run('sum()')
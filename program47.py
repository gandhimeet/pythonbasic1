'''
Write a Python program to find out the number of CPUs used.
'''
#importing multiprocessing module
import multiprocessing
#prints number of CPUs used.
print(multiprocessing.cpu_count())
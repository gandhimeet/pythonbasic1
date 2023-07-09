'''
Write a Python program to get the execution time of a Python method.
'''
#imported time modules
import time
#function sum of n numbers which does sum upto n numbers 
def sum_of_n_numbers(n):
    #start_time which starts timer
    start_time = time.time()
    #sum is equal to 0
    s = 0
    #caluclating sum from 1 to n  
    for i in range(1,n+1):
        s += i
    #end_time which ends time
    end_time = time.time()
    result =end_time-start_time
    return s,result
#taking input from user for the value of n 
n = int(input("Enter the value of n:\n"))
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))

'''
Write a Python program to create a histogram from a given list of integers.
'''
#function name histogram having paramter item array.
def histogram(item):
    for n in item:
        output =''
        times = n 
        while (times>0):
            output += '*'
            times = times -1
        print(output)
# calling functions and printing histograms as per given inputs.
histogram([2,3,5,9])
histogram([1,2,3,4,5,6,7,8])
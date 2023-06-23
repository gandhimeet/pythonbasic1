'''
Write a Python program that returns 
a string that is n (non-negative integer) copies of a given string.
'''
#larger string function name having parameter text used for getting string and n for repetation of string 
def larger_string(text, n):
    result = " "
    #using for loop for continously text getting till n 
    for i in range(n):
        result = result+text
    return result
#Meet Gandhi getting diplayed with 2 repetation
print(larger_string('Meet Gandhi',2))
#Rutvi Rathod getting displayed with 3 repetation
print(larger_string('Rutvi Rathod',3))

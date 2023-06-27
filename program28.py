'''
Write a Python program that concatenates all elements in a list into a string and returns it.
'''
#concate function name having parameter list 
def concate(list):
    #declaring result as empty string 
    result =''
    #adds the element in list by converting it into string  
    for element in list:
        result += str(element)
    # return result 
    return result

#calling concate function 
print(concate([2,3,4,5,7,9,15]))
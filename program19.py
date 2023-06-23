'''
Write a Python program to get a newly-generated string 
from a given string where "Is" has been added to the front. 
Return the string unchanged if the given string already begins with "Is".
'''
#new_string function name having parameter text for storing string 
#length of text >= 2 
#and is used for checking both condition 
#text[:2] == "IS" -text doesn't contain 

def new_string(text):
    if len(text) >=2 and text[:2] == "Is":
        return text 
    return "Is" + text
#calling function with parameter Array
print(new_string("Array"))
#calling function with parameter IsEmpty
print(new_string("IsEmpty"))
'''
Write a Python program to test whether a passed letter is a vowel or not.
'''
#function name is is_vowel having parameter char 
def is_vowel(char):
    everyvowel = 'aeiouAEIOU'
    return char in everyvowel

#calling function is_vowel
print(is_vowel('a'))
print(is_vowel('A'))
print(is_vowel('c'))
print(is_vowel('F'))
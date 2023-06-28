'''
Write a Python program that returns true if the two given integer values 
are equal or their sum or difference is 5.
'''
#function test_number having parameters x and y 
def test_number(x,y):
    #x = y or x-y=5 or x+y=5 then true otherwise false
    if x == y or abs(x-y)==5 or (x+y)==5:
        #return True 
        return True
    else:
        #return Falses
        return False
    
#calling function test_number
print(test_number(5,10)) # difference is 5
print(test_number(2,3)) #sum is 5 
print(test_number(5,5)) #both are equal
print(test_number(4,19)) #false case
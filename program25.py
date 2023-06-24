'''
Write a Python program that checks whether a specified value 
is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''
#isgroupmemeber is the function name checks whether the n is a memeber of groupdata.
def isgroupmember(groupdata,n):
    #checks each and every point 
    for value in groupdata:
        #check n is equal to value 
        if n == value:
            #returns True
            return True
    #returns False
    return False

#calling the function isgroupmember 
print(isgroupmember([1,2,3,4,5,3,3],3))
print(isgroupmember([1,2,3,4,5],-1))

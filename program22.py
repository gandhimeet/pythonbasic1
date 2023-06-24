'''
Write a Python program to count the number 4 in a given list.
'''
#function name is count_num_4 having parameter nums list.
def count_num_4(nums):
    #intilazing the count variable 0
    count = 0
    #for loop for the counting of 4 in list
    for num in nums:
        if num == 4:
            #count addition
            count += 1
    #returns count value in function
    return count

#calling function with parameters.
print(count_num_4([1,3,4,3,2,3,3,4,3,3,]))
print(count_num_4([1,3,4,3,2,3,3,4,4,4,]))

'''
Write a Python program that prints out all colors from color_list_1 that are not 
present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
'''
#Declaring color_list_1 and color_list_2 as set 
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
#displaying the set as it is...
#print("Diplaying the list as it is:")
#print(color_list_1)
#print(color_list_2)
#difference between color_list_2 and color_list_1
#print(color_list_2.difference(color_list_1))
#difference between color_list_1 and color_list_2 
print(color_list_1.difference(color_list_2))
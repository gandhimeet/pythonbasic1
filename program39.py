'''
Write a Python program to compute the future value of a specified principal amount,
rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
'''
amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) **years)
#printing the value with round off of 2 points 
print(round(future_value,2))
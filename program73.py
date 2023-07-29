'''
Write a Python program to calculate the midpoints of a line.
'''
print('\nCalculate the midpoint of a line :')
#input of starting point of line
x1 = float(input('The value of x (the first endpoint) '))
y1 = float(input('The value of y (the first endpoint) '))
#input of ending point of line
x2 = float(input('The value of x (the first endpoint) '))
y2 = float(input('The value of y (the first endpoint) '))
#finding midpoint of line
x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2
print();
#output of midpoint in a line 
print("The midpoint of line is :")
print( "The midpoint's x value is: ",x_m_point)
print( "The midpoint's y value is: ",y_m_point)
print();

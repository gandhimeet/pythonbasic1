'''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''
#n for storing the value of n 
n = int(input("Enter the value of n:"))
#n1 for storing n as n1
n1 = int("%s" %n)
#n2 for storing nn as n2
n2 = int("%s%s" % (n,n) )
#n3 for storing nnn as n3
n3 = int("%s%s%s" % (n,n,n) )
#displaying the algebra sum of n as n+nn+nnn
print("The Value of n+nn+nnn is:"+str(n1+n2+n3))

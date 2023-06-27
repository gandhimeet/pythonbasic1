'''
Write a Python program to find the least common multiple (LCM) of two positive integers.
'''
#lcm function name having parameter is x and y.
def lcm(x, y):
    #check x is greator then y then z = x otherwise z = y.
    if x > y:
        z = x
    else:
        z = y
    #checks z modulo x = 0 and y = 0
    while(True):
        if((z % x == 0) and (z % y == 0)):
            #lcm = z through checking modulo with z & y
            lcm = z
            break
        z += 1
    return lcm

#calling lcm function with different parameters.
print(lcm(4, 6))
print(lcm(15, 17))

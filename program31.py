'''
Write a Python program that computes the greatest common divisor (GCD) 
of two positive integers.
'''
#function name gcd having parameter x and y between whom we wanted to find Greatest Commaon Divisor
def gcd(x, y):
    gcd = 1   
    if x % y == 0:
        return y   
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break 
    return gcd
#calling gcd function with different parameters.
print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))

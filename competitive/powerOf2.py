import math as m

def isPowerofTwo(n):
    # n = 0 if undefined for log
    if n == 0 :
        return False
    
    power = m.log2(n)
    if (power - int(power)) == 0:
        return True
    return False

n = 8
print(isPowerofTwo(n))

s = 'string'
s= s[-1::-1]

s = 'Nepal'+s
print(s)
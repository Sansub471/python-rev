# To check an integer is power of 3 or not
import math as m

def isPowerOf3(N):
    if N == 0:
        return False
    power = m.log(N, 3)

    if (power - int(power)) == 0:
        return True
    return False

n = 8
print(isPowerOf3(n))
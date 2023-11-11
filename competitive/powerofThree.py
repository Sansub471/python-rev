# To check an integer is power of 3 or not
import math as m

# Hint : Try thinking out of this simple observation.
# 3^(p+1) % 3^p  == 0 always.

def isPowerOf3(N):
    if N == 0:
        return False
    power = m.log(N, 3)
    print(power)

    if (power - int(power)) == 0:
        return True
    return False

n = 243
print(isPowerOf3(n))

# The maximum value an integer can hold is : 2^(32) - 1
# Check 3 ^ 20, which is greater than the largest value an integer can hold
# Value greater than that will cause overflow.
# After hint:
        
        # """ The maximum power of 3 value that  
        #     integer can hold is 1162261467 ( 3^19 ) ."""

        # # Check if the given number is a power of 3
        # if 1162261467 % N == 0:
        #     return "Yes"
        # else:
        #     return "No"
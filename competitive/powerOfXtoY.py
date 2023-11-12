# Given a positive integer N, find if it can be expressed as xy where y > 1 and x > 0 and x and y both are both integers.

# Example 1:

# Input:
# N = 8
# Output:
# 1
# Explanation:
# 8 can be expressed
# as 2^3.

# Example 2:

# Input:
# N = 7
# Output:
# 0
# Explanation:
# 7 can't be expressed
# int the form xy.

# The hint, is similar to finding whether a number is prime or not?

def powerOfXtoY(N):
    if N == 1:
        return 1
    i = 2
    while(i*i <= N):
        j = 2
        while(j <= N):
            if i**j == N:
                return (i,j)
                #return 1
            j+= 1
        i+= 1
    return 0

N = 625
N = 243
#N = 8
print(powerOfXtoY(N))
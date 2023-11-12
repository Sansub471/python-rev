# Given a positive integer N, check if it is a perfect square or not.
# Note: Try to solve the question using only addition and subtraction operation.
# Example 1:

# Input:
# N = 35
# Output:
# 0
# Explanation:
# 35 is not a perfect 
# square.
 
# Example 2:
# Input:
# N = 49
# Output:
# 1
# Explanation:
# 49 is a perfect
# square.
import math as m

def checkPerfectSquare(N):
    for i in range(1, m.floor(m.sqrt(N)) + 1):
        if i**2 == N:
            return 1
    # Reached here means to perfect square
    return 0

N = 25
print(checkPerfectSquare(N))
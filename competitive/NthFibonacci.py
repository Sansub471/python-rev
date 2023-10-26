# Find the Nth Fibonacci Number, given a positive integer N
# Given a positive integer n, find the nth fibonacci number. 
# Since the answer can be very large, return the answer modulo 1000000007.

# Example 1:

# Input: 
# n = 2
# Output: 
# 1 
# Explanation: 
# 1 is the 2nd number of fibonacci series.
# Example 2:

# Input: 
# n = 5
# Output: 
# 5
# Explanation: 
# 5 is the 5th number of fibonacci series.

# This is iterative solution, correct but takes too much time
def nthFibonacci(n:int)->int:
    const = 1000000007
    t1 = t2 = 1
    if n == 1 or n == 2:
        return 1
    for i in range(3, n+1):
        fb = t1 + t2
        t1, t2 = t2, fb
    return fb % const

print(nthFibonacci(17))

# This is recursive solution. 
# Takes a lot of memory, or something?
def fibonacci(n:int):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n - 2)

print(fibonacci(2))

# This is the complete solution, not sure what this is :
class Solution:
    def nthFibonacci(self, n : int) -> int:
        mod = 10**9 + 7

        #initialize the dp array with 0 and 1 for base cases
        dp = [0] * (n + 5) # list with zeros of size (n+5)
        dp[0] = 0
        dp[1] = 1

        #compute the fibonacci numbers using dynamic programming
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] % mod + dp[i - 2] % mod) % mod
        
        #return the nth fibonacci number
        return dp[n]
    
sl = Solution()
print(sl.nthFibonacci(20))
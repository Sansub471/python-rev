# Given a number N, find the total sum of digits of all the numbers from 1 to N.
 

# Example 1:

# Input:
# N = 5
# Output:
# 15
# Explanation:
# Sum of digits of number from 1 to 5:
# 1 + 2 + 3 + 4 + 5 = 15
# Example 2:

# Input:
# N = 12
# Output
# 51
# Explanation:
# Sum of all digits from 1 to 12 is:
# 1+2+3+4+5+6+7+8+9+(1+0)+(1+1)+(1+2) = 51

def sumOfDigit(N):
    # From given hints
    if N < 10:
        return (N(N+1) // 2) # sum of natural numbers from 1 to N
    

def sumOfDigits(N):
    sum = 0
    for i in range(1, N+1):
        if i < 10:
            sum += i
        else:
            digitS = 0
            number = i
            while(number != 0):
                digitS += number % 10
                number //= 10
            sum += digitS
    return sum

N = 99
print(sumOfDigit(N))

# Given solution
#Back-end complete function Template for Python 3
import math
class Solution:
    def sumOfDigits (self,N):
        # base case: if n<10 return sum of 
        # first n natural numbers 
        if (N<10) : 
            return (N*(N+1)//2) 
        
        # d = number of digits minus one in n. 
        # For 328, d is 2 
        d = (int)(math.log10(N)) 
        
        """computing sum of digits from 1 to 10^d-1, 
        d=1 a[0]=0; 
        d=2 a[1]=sum of digit from 1 to 9 = 45 
        d=3 a[2]=sum of digit from 1 to 99 = a[1]*10  
        + 45*10^1 = 900 
        d=4 a[3]=sum of digit from 1 to 999 = a[2]*10  
        + 45*10^2 = 13500"""
        a = [0] * (d + 1) 
        a[0] = 0
        a[1] = 45
        for i in range(2, d+1) : 
            a[i] = a[i-1] * 10 + 45 * (int)(math.ceil(math.pow(10,i-1))) 
        
        # computing 10^d 
        p = (int)(math.ceil(math.pow(10, d))) 
        
        # Most significant digit (msd) of n, 
        # For 328, msd is 3 which can be obtained 
        # using 328/100 
        msd = N//p 
        
        """EXPLANATION FOR FIRST and SECOND TERMS IN 
        BELOW LINE OF CODE 
        First two terms compute sum of digits from 1 to 299 
        (sum of digits in range 1-99 stored in a[d]) + 
        (sum of digits in range 100-199, can be calculated  
        as 1*100 + a[d]. (sum of digits in range 200-299, 
        can be calculated as 2*100 + a[d] 
        The above sum can be written as 3*a[d] + (1+2)*100 
        
        EXPLANATION FOR THIRD AND FOURTH TERMS IN BELOW 
        LINE OF CODE 
        The last two terms compute sum of digits in number 
        from 300 to 328. The third term adds 3*29 to sum 
        as digit 3 occurs in all numbers from 300 to 328. 
        The fourth term recursively calls for 28"""
        return (int)(msd * a[d] + (msd*(msd-1) // 2) * p +  
               msd * (1 + N % p) + self.sumOfDigits(N % p)) 
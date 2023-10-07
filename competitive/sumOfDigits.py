# Keep finding the sum of digits until the sum becomes a single digit 
# Use recursion

def SumOfDigits(N):
    if N < 10 :
        return N # base case
    else:
        sum = 0
        while( N != 0):
            sum += N % 10
            N = N // 10
        return SumOfDigits(sum)

print(SumOfDigits(12345))

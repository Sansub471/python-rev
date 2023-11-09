def isPrime (N):
    if(N == 1): # if N = 1 return 0
        return 0
    i = 2
    # loop from 2 to sqrt(N)
    while(i*i<=N): 
        if(N%i==0): # if N is divisble by any other number return 0 
            return 0
        i+=1
    return 1 # return 1 if N is not divisible by any other number.

# The factors from 2 to sqrt(n) have multiples from sqrt(n)+1 to n.

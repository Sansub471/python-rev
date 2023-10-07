# Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.
# Input:
# N = 10
# A[] = {6,1,2,8,3,4,7,10,5}
# Output: 9

def missingNumber(arr, N):
    s = int(N*(N+1)/2) # sum of first n natural numbers
    arr_sum = sum(arr)
    return s - arr_sum

# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) 
# which has the maximum sum and return its sum.

# Example 1
# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which 
# is a contiguous subarray.

# Input:
# N = 4
# Arr[] = {-1,-2,-3,-4}
# Output:
# -1
# Explanation:
# Max subarray sum is -1 
# of element (-1)

def maxSubArraySum(arr, N):
    # Kadane's Algorithm
    # https://en.wikipedia.org/wiki/Maximum_subarray_problem
    best_sum = float('-inf')
    current_sum = 0
    for x in arr:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

arr = [1,2,3,-2,5]
N = len(arr)
print(maxSubArraySum(arr, N))

# Simple Approach:
# https://www.interviewbit.com/blog/maximum-subarray-sum/

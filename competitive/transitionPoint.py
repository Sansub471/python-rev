# Given a sorted array containing only 0s and 1s, find the transition point, i.e., 
# the first index where 1 was observed, and before that, only 0 was observed.

# Example 1:

# Input:
# N = 5
# arr[] = {0,0,0,1,1}
# Output: 3
# Explanation: index 3 is the transition 
# point where 1 begins.
# Example 2:

# Input:
# N = 4
# arr[] = {0,0,0,0}
# Output: -1
# Explanation: Since, there is no "1",
# the answer is -1.

def transitionPoint(arr, n):
    for i in range(0, len(arr)):
        if arr[i] == 1:
            return i
    # Reached here means all zero
    return -1
# Given an array A of n positive numbers. The task is to find the first equilibrium point in an array. 
# Equilibrium point in an array is an index (or position) such that the sum of all elements before that 
# index is same as sum of elements after it.

# Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 

# Example 1:

# Input: 
# n = 5 
# A[] = {1,3,5,2,2} 
# Output: 
# 3 
# Explanation:  
# equilibrium point is at position 3 as sum of elements before it (1+3) = sum of elements after it (2+2). 
# Example 2:

# Input:
# n = 1
# A[] = {1}
# Output: 
# 1
# Explanation:
# Since there's only element hence its only the equilibrium point.

# A : array
# N : len(A)
def equilibriumPoint(A, N):
    if len(A) == 1:
        return 1
    low = 0
    high = len(A) - 1
    mid = (low + high) // 2
    while(mid != 0):
        front = sum(A[low:mid])
        if mid == high:
            back = A[high]
        else:
            back = sum(A[mid+1:high+1])
    
        if front > back:
            high = mid
            A[mid]+= back
        elif back > front:
            low = mid
            A[mid] += front
        else:
            return mid + 1 # front == back
        mid = (low + high) // 2
    # Comming here means no equilibrium
    return -1

A = [9,10]
N = len(A)
print(equilibriumPoint(A, N))
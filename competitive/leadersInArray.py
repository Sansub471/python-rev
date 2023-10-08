# Given an array A of positive integers. Your task is to find the leaders in the array. 
# An element of array is leader if it is greater than or equal to all the elements to its right side. 
# The rightmost element is always a leader. 

# Example 1:

# Input:
# n = 6
# A[] = {16,17,4,3,5,2}
# Output: 17 5 2
# Explanation: The first leader is 17 
# as it is greater than all the elements
# to its right.  Similarly, the next 
# leader is 5. The right most element 
# is always a leader so it is also 
# included.
# Example 2:

# Input:
# n = 5
# A[] = {1,2,3,4,0}
# Output: 4 0
# Explanation: 0 is the rightmost element
# and 4 is the only element which is greater
# than all the elements to its right.

# Works but not optimum
def leadersInArray(A, N):
    # If only one element, it is the leader
    if len(A) <= 1:
        return A
    candidate = A[0]
    leaders = []
    for i in range(1, len(A)):
        if i == len(A) - 1 :
            leaders.append(A[i])
        sub_arr = A[i:]
        sub_arr.sort(reverse=True)
        if candidate > sub_arr[0] and candidate not in leaders:
            leaders.append(candidate)
        candidate = A[i]
    return leaders

# After tips
def leaders(A, N):
    # If there is only one element
    if len(A) <= 1:
        return A
    new_max = A[len(A) - 1]
    leaders = [new_max]
    for i in range(len(A) - 2, -1, -1):
        if A[i] >= new_max:
            new_max = A[i]
            leaders.append(A[i])
    return leaders[-1::-1]

A = [16,17,4,3,5,2]
N = len(A)
print(leaders(A, N))
    
    

# Given an array arr of n integers, write a function that returns true if there is a triplet (a, b, c) 
# from the array (where a, b, and c are on different indexes) that satisfies a2 + b2 = c2, otherwise return false.

# Example 1:

# Input:
# N = 5
# Arr[] = {3, 2, 4, 6, 5}
# Output: Yes
# Explanation: a=3, b=4, and c=5 forms a
# pythagorean triplet.
# Example 2:

# Input:
# N = 3
# Arr[] = {3, 8, 5}
# Output: No
# Explanation: No such triplet possible.

# Hashing a big concept in programming.

# Don't know how to find pythgorean concept in programming.

# def PythagoreanTriplets(arr, N):
#     for i in range(0, len(arr) - 1):
#         for j in range(0, len(arr)):
#             if j != i or j != i+1:
#                 if 
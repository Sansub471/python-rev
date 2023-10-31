# Given a sorted array of size N and an integer K, find the position(0-based indexing) 
# at which K is present in the array using binary search.

# Example 1:

# Input:
# N = 5
# arr[] = {1 2 3 4 5} 
# K = 4
# Output: 3
# Explanation: 4 appears at index 3.

# Example 2:

# Input:
# N = 5
# arr[] = {11 22 33 44 55} 
# K = 445
# Output: -1
# Explanation: 445 is not present.

def binarySearch(arr, n, k):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = low + (high - low ) // 2
        if k < arr[mid]:
            high = mid - 1 
        elif k > arr[mid]:
            low = mid + 1
        else:
            return mid
    # Reached here means element not found
    return -1

arr = [1,2,3,4,5]
k = 4
n = len(arr)
print(binarySearch(arr, n, k))

# Time Complexity: O(log N)
# Auxiliary Space: O(1)
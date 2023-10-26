# Given an array arr[] and an integer K where K is smaller than size of array, the task is 
# to find the Kth smallest element in the given array. It is given that all array elements are distinct.

# Note :-  l and r denotes the starting and ending index of the array.

# Example 1:

# Input:
# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# Output : 7
# Explanation :
# 3rd smallest element in the given 
# array is 7.
# Example 2:

# Input:
# N = 5
# arr[] = 7 10 4 20 15
# K = 4
# Output : 15
# Explanation :
# 4th smallest element in the given 
# array is 15.

def kthSmallest(arr, l, r, k):
    for i in range(0, k):
        smallest = arr[l]
        for j in range(l+1, r+1):
            if arr[j] < smallest:
                arr[l], arr[j] = arr[j], arr[l]
                smallest = arr[l]
        l += 1
    return arr[k-1]

# With hint, the solution could be quick select
def kthSmallestElement(arr, l, r, k):
    pass



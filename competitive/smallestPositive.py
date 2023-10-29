# You are given an array arr[] of N integers. The task is to find the smallest positive number missing from the array.

# My assumption is the numbers will not be larger than N ????

# Note: Positive number starts from 1.

# Example 1:

# Input:
# N = 5
# arr[] = {1,2,3,4,5}
# Output: 6
# Explanation: Smallest positive missing 
# number is 6.
# Example 2:

# Input:
# N = 5
# arr[] = {0,-10,1,3,-20}
# Output: 2
# Explanation: Smallest positive missing 
# number is 2.

def smallestPositiveNumber(arr, n):
    # step 1 : bring -ve and zero elements to the left, and rest to the right
    low = 0
    for i in range(0, len(arr)):
        if arr[i] <= 0:
            arr[low], arr[i] = arr[i], arr[low]
            low += 1
    # step 2 : the positive part starts at index 'low' to the end
    pos_len = len(arr[low:])

    # step 3 : Use index to store information of digit occurence
    for elem in arr[low:]:
        if elem < pos_len:
            arr[low + elem - 1] = -arr[low + elem - 1]
    
    # step 4 : check where are the negatives
    for i, elem in enumerate(arr[low:]):
        if elem > 0:
            return i+1
    
    # All negative means, N+1 is the smallest integer
    return pos_len + 1


arr = [0, -10, 1, 3, -20]
n = len(arr)
print(smallestPositiveNumber(arr, n))
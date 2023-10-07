# Given an array a of size N which contains elements from 0 to N-1, 
# you need to find all the elements occurring more than once in the given array. 
# Return the answer in ascending order. If no such element is found, return list containing [-1]. 

# Example 1
# Input:
# N = 4
# a[] = {0,3,1,2}
# Output: 
# -1
# Explanation: 
# There is no repeating element in the array. Therefore output is -1.

# Example 2
# Input:
# N = 5
# a[] = {2,3,1,2,3}
# Output: 
# 2 3 
# Explanation: 
# 2 and 3 occur more than once in the given array.

class Solution:
    def duplicates(self, arr, n):
        # Using given array as hash table

    	# First check all the values that are 
    	# present in an array then go to that 
    	# values as indexes and increment by 
    	# the size of array
        for i in range(0, n):
            index = arr[i] % n
            arr[index] += n
    	# Now check which value 
    	# exists more 
    	# than once by dividing 
    	# with the size 
    	# of array 
        flag = False
        res = []
        for i in range(0,n): 
            if (arr[i]//n) > 1: 
                res.append(i)
                flag=True
        if flag==False:
            res.append(-1)
        return res
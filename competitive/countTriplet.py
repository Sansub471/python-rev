# Given an array of distinct integers. The task is to count all the triplets such that sum of two 
# elements equals the third element.
 
# Example 1:

# Input: 
# N = 4 
# arr[] = {1, 5, 3, 2}
# Output: 2 
# Explanation: There are 2 triplets:
#  1 + 2 = 3 and 3 +2 = 5

# Example 2:

# Input: 
# N = 3
# arr[] = {2, 3, 4}
# Output: 0
# Explanation: No such triplet exits


# //Back-end complete function template for C++

# class Solution{
# public:
# 	//Function to count the number of triplets with the given condition.
# 	int countTriplet(int arr[], int n)
# 	{
# 		//Sorting the array in ascending order.
# 		sort(arr, arr + n); 
		
# 		//Initializing the count of triplets as 0.
# 		int  ans = 0;

# 		//Iterating over the array in reverse order.
# 		for (int i = n - 1; i >= 0; i--)
# 		{
# 			//Initializing two pointers, one at the beginning and one at i-1.
# 			int j = 0;
# 			int k = i - 1;

# 			//Using two-pointer approach to find the triplets.
# 			while (j < k)
# 			{
# 				//If the given condition is satisfied, increment the count and move the pointers.
# 				if(arr[i] == arr[j] + arr[k])
# 				{
# 					ans++;
# 					j++;
# 					k--;
# 				}
# 				//If the sum is less than the target, move the left pointer.
# 				else if (arr[i] > arr[j] + arr[k])
# 					j++;
# 				//If the sum is greater than the target, move the right pointer.
# 				else
# 					k--;
# 			}
# 		}

# 		//Returning the count of triplets.
# 		return ans;
# 	}
	 
# };
def countTriplets(arr, n):
    arr.sort(reverse=False) # Sort the elements first

    # Initializing the count of tirplets as zero
    ans = 0

    # Iterating over the array in reverse order
    for i in range(len(arr) - 1, 0, -1):
        # Initializing the two pointers, one at the end one at the beginning
        low = 0
        high = i - 1

        # Using the two pointer approach to find the triplets
        while( low < high):
            # If the given condition is satisfied, increment the count and move the pointers
            if arr[i] == arr[low] + arr[high]:
                ans += 1
                low += 1
                high -= 1
            # If the sum is less than the target, move the left pointer
            elif arr[i] > arr[low] + arr[high]:
                low += 1
            # If the sum is greater than the target, move the right pointer
            else:
                high -= 1
    # Returning the count of triplets
    return ans

arr = [1,5,3,2]
N = len(arr)
print(countTriplets(arr, N))

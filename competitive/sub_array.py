# Sub-array with the given sum
#Function to find a continuous sub-array which adds up to a given number.
class Solution1:
    def subArraySum(self,arr, n, s):
        for i in range(n):
            sub_arr = arr[i:]
            sum = 0
            left = 0
            for j, num in enumerate(sub_arr):
                sum += num
                if sum > s:
                    sum -= sub_arr[left]
                    left += 1
                if sum == s:
                    return [i+1, i+j+1]
        return [-1]

sln1 = Solution1()
n = 42
s = 468
arr = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
print(sln1.subArraySum(arr, n, s))


# Complete solution
#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, sum_): 
        # Initialize curr_sum as
        # value of first element
        # and starting point as 0 
        A = []
        curr_sum = arr[0]
        start = 0

        # Add elements one by 
        # one to curr_sum and 
        # if the curr_sum exceeds 
        # the sum, then remove 
        # starting element 
        i = 1
        while i <= n:
        
            # If curr_sum exceeds
            # the sum, then remove
            # the starting elements
            while curr_sum > sum_ and start < i-1:
        
                curr_sum = curr_sum - arr[start]
                start += 1
            
            # If curr_sum becomes
            # equal to sum, then
            # return true
            if curr_sum == sum_:
                A.append(start+1)
                A.append(i)
                return A

            # Add this element 
            # to curr_sum
            if i < n:
                curr_sum = curr_sum + arr[i]
            i += 1

        # If we reach here, 
        # then no subarray
        A.append(-1)
        return A

sln = Solution()
print("The complete solution : ")
print(sln.subArraySum(arr, n, s))
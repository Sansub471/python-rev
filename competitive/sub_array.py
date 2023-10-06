#Function to find a continuous sub-array which adds up to a given number.
class Solution:
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

sln = Solution()
n = 42
s = 468
arr = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
print(sln.subArraySum(arr, n, s))

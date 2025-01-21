from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            three_sum_target = target - nums[i]
            
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                two_sum_target = three_sum_target - nums[j]
                
                # Two-pointer search
                left, right = j + 1, n - 1
                while left < right:
                    lr_sum = nums[left] + nums[right]
                    if lr_sum == two_sum_target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for left and right
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move pointers inward
                        left += 1
                        right -= 1
                    elif lr_sum < two_sum_target:
                        left += 1
                    else:
                        right -= 1
                        
        return result
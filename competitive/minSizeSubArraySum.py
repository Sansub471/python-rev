class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        head, min_length = 0, len(nums) + 1
        total = 0

        for tail in range(len(nums)):
            while head < len(nums) and total < target:
                total += nums[head]
                head += 1
            
            if total >= target:
                min_length = min(min_length, head - tail)
                total -= nums[tail]
            else:
                break

        return 0 if min_length == len(nums) + 1 else min_length

from typing import List
def findMin(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        # pivot and min must be on the right
        if nums[mid] > nums[right]:
            left = mid + 1 
        elif nums[mid] < nums[right]:
            right = mid
        else:
            # reduce the search space
            right -= 1
    return nums[left]
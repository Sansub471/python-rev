# Find minimum in rotated sorted array or the pivot of rotation
from typing import List

def findMin(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        # pivot to the right
        if nums[mid] > nums[right]:
            left = mid + 1
        # pivot is on the left or mid itself
        else:
            right = mid
    # left = right means pivot found
    return nums[left] # nums[right]
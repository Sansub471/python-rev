from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid + 1] < arr[mid]:
                high = mid  # The peak is in the left half (or at mid)
            else:
                low = mid + 1  # The peak is in the right half
        
        return low
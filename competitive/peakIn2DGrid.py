from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        low, high = 0, len(mat) - 1
        
        while low <= high:
            mid_row = low + (high - low) // 2
            
            # Find the column-local peak in the middle row
            max_col = 0
            for col in range(len(mat[mid_row])):
                if mat[mid_row][col] > mat[mid_row][max_col]:
                    max_col = col
            
            # Check neighbors to determine if it's a global peak
            peak_value = mat[mid_row][max_col]
            is_top_smaller = (mid_row == 0 or mat[mid_row - 1][max_col] < peak_value)
            is_bottom_smaller = (mid_row == len(mat) - 1 or mat[mid_row + 1][max_col] < peak_value)
            
            if is_top_smaller and is_bottom_smaller:
                return [mid_row, max_col]
            
            # Move search to the row with the larger neighbor
            if mid_row > 0 and mat[mid_row - 1][max_col] > peak_value:
                high = mid_row - 1  # Move up
            else:
                low = mid_row + 1  # Move down
        
        return [-1, -1]  # Should never reach here


# Finding peak in a 2D grid matrix
# Find the time complexity of the code
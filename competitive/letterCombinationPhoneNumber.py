from typing import List

class Solution:
    def backtrack(self, digits: str, digit_map: dict, current: str, index: int, result: List[str]):
        # Base case
        if index == len(digits):
            result.append(current)
            return

        # Get the mapped string for the current digit
        letters = digit_map.get(digits[index], "")
        for letter in letters:
            # Add the current letter and recurse
            self.backtrack(digits, digit_map, current + letter, index + 1, result)
        
        # Handle unmapped digits (e.g., '0' and '1')
        if not letters:
            self.backtrack(digits, digit_map, current, index + 1, result)

    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '0': "", '1': "", '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        result = []
        if not digits:
            return result
        self.backtrack(digits, digit_map, "", 0, result)
        return result
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Input: digits = "2"
Output: ["a","b","c"]
"""

# Runtime: 43 ms, faster than 23.23% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14.4 MB, less than 30.59% of Python3 online submissions for Letter Combinations of a Phone Number.
class Solution:
    def backtrack(
        self, result: List[str], digit_map: dict, digits: str, combination, index: int
    ):
        if index > len(digits):
            return

        if len(combination) == len(digits):
            result.append(combination)
            return

        current_digit = digits[index]
        current_string = digit_map[current_digit]

        for i in range(len(current_string)):
            self.backtrack(
                result, digit_map, digits, combination + current_string[i], index + 1
            )

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not len(digits):
            return result
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        self.backtrack(result, digit_map, digits, "", 0)

        return result

"""
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
https://leetcode.com/problems/move-zeroes/
"""

# Runtime: 168 ms, faster than 10.57% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.7 MB, less than 20.74% of Python3 online submissions for Move Zeroes.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        size = len(nums)
        while i < size:
            if nums[i] == 0:
                nums.append(0)
                del nums[i]
                size -= 1
            else:
                i += 1


class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        size = len(nums)
        while i < size:
            if nums[i]:
                i += 1
            else:
                nums.append(0)
                del nums[i]
                size -= 1

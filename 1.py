"""Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing import List


# Runtime: 5616 ms, faster than 11.58% of Python3 online submissions for Two Sum.
# Memory Usage: 14.9 MB, less than 67.87% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_i, i in enumerate(nums):
            index_j = index_i + 1
            while index_j < len(nums):
                if (i + nums[index_j]) == target:
                    return [index_i, index_j]
                index_j += 1


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))

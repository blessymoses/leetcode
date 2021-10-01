"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
nums = [1,2,3]
[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
from typing import List


# Runtime: 47 ms, faster than 22.32% of Python3 online submissions for Subsets.
# Memory Usage: 14.4 MB, less than 77.83% of Python3 online submissions for Subsets.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in nums:
            temp = []
            for item in subsets:
                temp.append(item + [n])
            subsets.extend(temp)
        return subsets


s = Solution()
print(s.subsets([1, 2, 3]))

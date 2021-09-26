"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
https://leetcode.com/problems/boats-to-save-people/
"""
from typing import List

# Runtime: 440 ms, faster than 89.19% of Python3 online submissions for Boats to Save People.
# Memory Usage: 21 MB, less than 80.39% of Python3 online submissions for Boats to Save People.
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        i, j = 0, len(people) - 1
        while i <= j:
            if i == j:
                return boats + 1
            if people[i] + people[j] <= limit:
                i += 1
            boats += 1
            j -= 1
        return boats


s = Solution()
print(s.numRescueBoats([1, 2], 3))

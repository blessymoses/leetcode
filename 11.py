"""
Container with most water
Given n non-negative integers a1, a2, ..., an , where each 
represents a point at coordinate (i, ai). n vertical lines are 
drawn such that the two endpoints of the line i is at (i, ai) 
and (i, 0). Find two lines, which, together with the x-axis 
forms a container, such that the container contains the most water.
[1,8,6,2,5,4,8,3,7] 49
[1,1] 1
[4,3,2,1,4]
[1,2,1]
"""

# Runtime: 760 ms, faster than 53.35% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.5 MB, less than 57.02% of Python3 online submissions for Container With Most Water.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            min_height = min(height[left], height[right])
            current_area = min_height * (right - left)
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

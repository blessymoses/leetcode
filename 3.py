"""
Given a string s, find the length of the longest substring without repeating characters.
"""

# Runtime: 124 ms, faster than 25.71% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.4 MB, less than 24.39% of Python3 online submissions for Longest Substring Without Repeating Characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if not s:
            return 0
        start, end = 0, 0
        max_length = 0
        unique_str = set()
        while end < len(s):
            if s[end] in unique_str:
                unique_str.remove(s[start])
                start += 1
            else:
                unique_str.add(s[end])
                end += 1
                max_length = max(max_length, len(unique_str))
        return max_length

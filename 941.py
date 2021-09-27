"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
https://leetcode.com/problems/valid-mountain-array/
"""
# Runtime: 196 ms, faster than 86.74% of Python3 online submissions for Valid Mountain Array.
# Memory Usage: 15.6 MB, less than 59.56% of Python3 online submissions for Valid Mountain Array.
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[1] < arr[0]:
            return False
        uphill = True
        for i, num in enumerate(arr[:-1]):
            if arr[i + 1] == num:
                return False
            if uphill == False and (arr[i + 1] > num):
                return False
            if uphill and (arr[i + 1] < num):
                uphill = False
        if uphill:
            return False
        return True


# Runtime: 204 ms, faster than 63.12% of Python3 online submissions for Valid Mountain Array.
# Memory Usage: 15.5 MB, less than 59.56% of Python3 online submissions for Valid Mountain Array.
class Solution2:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 1
        while i < len(arr) and arr[i] > arr[i - 1]:
            i += 1
        if i == 1 or i == len(arr):
            return False
        while i < len(arr) and arr[i] < arr[i - 1]:
            i += 1
        return i == len(arr)

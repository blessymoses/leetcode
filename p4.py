"""
Consider an array of non-negative integers.
A second array is formed by shuffling the elements of the first array and deleting a random element.
Given these two arrays, find which element is missing in the 
second array
"""
from typing import List


def find_missing(arr1: List, arr2: List) -> int:
    return sum(arr1) - sum(arr2)


print(find_missing([1, 3, 5, 7], [3, 7, 1]))

"""
Given an array of integers(positive and negative), 
write a program that can find the largest continuous sum
- return the total sum amount
[7,8,9]->24
[-1,7,8,9,-10]->24
[2,3,-10,9,2]->11
[2,11,-10,9,2]->14
[12,-10,7,-8,4,6]->12
"""
from typing import List


def find_largest_continuous_sum(arr: List) -> int:
    print(f"\n{arr}")
    if not arr:
        return 0
    current_sum = arr[0]
    max_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)
    return max_sum


print(find_largest_continuous_sum([7, 8, 9]))
print(find_largest_continuous_sum([-1, 7, 8, 9, -10]))
print(find_largest_continuous_sum([2, 3, -10, 9, 2]))
print(find_largest_continuous_sum([2, 11, -10, 9, 2]))
print(find_largest_continuous_sum([12, -10, 7, -8, 4, 6]))

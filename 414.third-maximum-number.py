#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
# 
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

# @lc code=start
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        for num in nums:
            if num in (first, second, third):
                continue
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
        return third if third != float('-inf') else first
        
# @lc code=end


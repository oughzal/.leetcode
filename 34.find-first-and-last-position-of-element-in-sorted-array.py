#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        l,r = 0, len(nums) -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                break
            if nums[mid]>target:
                r = mid -1
            else:
                l = mid +1
        if nums[mid] != target:
            return [-1,-1]
        l,r = mid,mid
        while l>0 and nums[l-1] == target :
            l -= 1
        while r<len(nums) -1 and nums[r+1]== target :
            r += 1
        return [l,r]
# @lc code=end


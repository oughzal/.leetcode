#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max(counter.keys(), key=counter.get)
# @lc code=end


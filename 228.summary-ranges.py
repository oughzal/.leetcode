#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result =  []
        L =[]
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i]+1 == nums[i+1]:
                L.append(nums[i])
            else:
                L.append(nums[i])
                if len(L) == 1:
                    result.append(str(L[0]))
                else:
                    result.append(str(L[0]) + '->' + str(L[-1]))
                L = []
        return result
        
        
# @lc code=end


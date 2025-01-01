#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            result = result * 26 + ord(columnTitle[i]) - ord('A') + 1
        return result
        
# @lc code=end


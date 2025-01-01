#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(result[::-1])
        
# @lc code=end


#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
        # n = len(s)
        # for i in range(1, n // 2 + 1):
        #     if n % i == 0:
        #         if s[:i] * (n // i) == s:
        #             return True
        # return False
        
# @lc code=end


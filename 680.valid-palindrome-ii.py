#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left:right]) or is_palindrome(s[left+1:right+1])
            left += 1
            right -= 1
        return True
        
# @lc code=end


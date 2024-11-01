#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        res = []
        self.dfs(phone, digits, 0, '', res)
        return res
    def dfs(self, phone, digits, index, path, res):
        if index == len(digits):
            res.append(path)
            return
        for letter in phone[digits[index]]:
            self.dfs(phone, digits, index + 1, path + letter, res)
        
# @lc code=end


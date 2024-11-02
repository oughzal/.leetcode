#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from typing import List
from collections import Counter

class Solution:
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length * word_count
        word_map = Counter(words)
        result = []

        for i in range(word_length):
            left = i
            right = i
            current_map = Counter()
            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length
                if word in word_map:
                    current_map[word] += 1
                    while current_map[word] > word_map[word]:
                        current_map[s[left:left + word_length]] -= 1
                        left += word_length
                    if right - left == total_length:
                        result.append(left)
                else:
                    current_map.clear()
                    left = right
        
        return result
        
# @lc code=end


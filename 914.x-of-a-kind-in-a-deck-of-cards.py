#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#

# @lc code=start
from typing import List
from collections import Counter
from math import gcd
from functools import reduce


class Solution:
    
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = Counter(deck).values()
        g = reduce(gcd, counts)
        return g >= 2

        
# @lc code=end


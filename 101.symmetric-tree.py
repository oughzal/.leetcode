#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)
    
    def isMirror(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False

        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
        
# @lc code=end


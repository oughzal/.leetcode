#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkHeight(root) != -1
    
    def checkHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        leftHeight = self.checkHeight(root.left)
        if leftHeight == -1:
            return -1
        
        rightHeight = self.checkHeight(root.right)
        if rightHeight == -1:
            return -1
        
        if abs(leftHeight - rightHeight) > 1:
            return -1
        
        return 1 + max(leftHeight, rightHeight)
        
# @lc code=end


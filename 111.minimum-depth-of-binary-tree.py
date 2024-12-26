#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        if leftDepth == 0 or rightDepth == 0:
            return 1 + max(leftDepth, rightDepth)

        return 1 + min(leftDepth, rightDepth)
    

        
# @lc code=end


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.MaxDepth=0

        def DFS(node):
            if node == None:
                return 0
            leftD=1+DFS(node.left)
            rightD=1+DFS(node.right)
            localMax=max(leftD,rightD)
            self.MaxDepth=max(self.MaxDepth, localMax)
            return localMax
        DFS(root)
        return self.MaxDepth
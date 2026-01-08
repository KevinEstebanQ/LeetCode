from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7 # answer can be very large, MOD the answer
        self.ans = 0 # final answer to be updated

        def totalSum(node):
            if not node: # recursively find the total sum of the tree
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        
        def DFS(node): #postorder DFS to find the subsums
            if not node:
                return 0
            
            left = DFS(node.left) # build the sum of the subtrees
            right = DFS(node.right)

            subSum = node.val + left + right

            self.ans = max(self.ans, subSum*(total-subSum)) #ans here is equal to the product, it will update once a new max is found

            return subSum

        total = totalSum(root)
        DFS(root)
        return self.ans%MOD

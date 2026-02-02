# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node1):
            if node1 in oldToNew:
                return oldToNew[node1]
            if not node1:
                return
            copy = Node(node1.val)
            oldToNew[node1] = copy
            for n in node1.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node)
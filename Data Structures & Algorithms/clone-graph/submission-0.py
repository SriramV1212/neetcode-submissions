"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        clonemap = {}

        def dfs(n):
            if n in clonemap:
                return clonemap[n]
            
            
            clonemap[n] = Node(n.val) # create clone node without initializing neighbors

            for neighbor in n.neighbors:
                dfs(neighbor)
            
            clonemap[n].neighbors = [clonemap[neighbor] for neighbor in n.neighbors]

        dfs(node)

        return clonemap[node]

        
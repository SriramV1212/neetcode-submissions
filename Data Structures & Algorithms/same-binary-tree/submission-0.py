# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recurse(node , l):
            if not node:
                l.append('null')
                return 

            l.append(node.val)

            recurse(node.left, l)
            recurse(node.right,l)

            return l

        list_p = recurse(p, [])
        list_q = recurse(q, [])

        return list_p == list_q


        
        
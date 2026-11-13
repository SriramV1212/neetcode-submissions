# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        d = 0

        def dfs(node):

            if not node.left:
                left_depth = 0
            else:
                left_depth = 1 + dfs(node.left)

            if not node.right:
                right_depth = 0
            else:
                right_depth = 1 + dfs(node.right)

            length = left_depth + right_depth

            nonlocal d
            d= max(length,d)

            return max(left_depth,right_depth)


        dfs(root)

        return d


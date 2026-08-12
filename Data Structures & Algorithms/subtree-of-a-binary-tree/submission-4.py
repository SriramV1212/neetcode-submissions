# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        q = deque([root])

        while q:
            node = q.popleft()
            if node.val == subRoot.val and self.isSame(node, subRoot):
                return True
              
            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)
        
        return False

    def isSame(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:

        if not a and not b:
            return True
        
        if a and b and a.val == b.val:
            return self.isSame(a.left, b.left) and self.isSame(a.right, b.right)

        else:
            return False



        
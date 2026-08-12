# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        q = deque([root])

        node = root

        while node.val!=subRoot.val:
            node = q.popleft()
            q.append(node.left)
            q.append(node.right)

        def isSame(a, b):
            if not a and not b:
                return True
            
            if a and b and a.val == b.val:
                return isSame(a.left, b.left) and isSame(a.right, b.right)

            else:
                return False

        return isSame(node, subRoot)

        
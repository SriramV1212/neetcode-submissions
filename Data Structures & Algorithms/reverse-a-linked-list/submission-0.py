# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None

        while curr:
            next_node = curr.next      # new pointer that points to next node to preserve its location before changing current node's next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev




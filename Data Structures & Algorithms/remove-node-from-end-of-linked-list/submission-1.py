# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodes = []

        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        if n == len(nodes):
            return head.next

        remove_node = nodes[-n]
        before_node = nodes[-n-1]

        before_node.next = before_node.next.next

        return head
        
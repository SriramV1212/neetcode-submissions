# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr = head.next

        nodes = []

        while curr:
            nodes.append(curr)
            curr = curr.next

        curr = head
        step = 0

        while nodes:
            if step % 2 == 0:
                link_node = nodes.pop()
            else:
                link_node = nodes.pop(0)

            curr.next = link_node
            step+=1
            curr = curr.next

        curr.next = None



                






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Count the number of nodes.
        node = head
        N = 1
        while (node.next):
            N += 1
            node = node.next

        # Remove the N - nth node from the start.
        node = head
        k = N - n

        if k == 0:
            return head.next

        for i in range(k - 1):
            node = node.next

        node.next = node.next.next

        return head

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        early = ListNode()
        late = ListNode()        

        # Early travels faster than late, so they shouldn't meet up unless a cycle.

        early = head
        late = head

        # Must check it can advance safely.
        while (early and early.next):
            
            early = early.next.next            
            late = late.next

            if early == late:
                return True

        return False
        
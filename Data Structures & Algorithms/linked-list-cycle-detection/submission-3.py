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
        late.next = head

        while (early and late):
            if early.next == None:
                return False
                
            if early == late:
                return True

            early = early.next.next            
            late = late.next
        
        return False
        
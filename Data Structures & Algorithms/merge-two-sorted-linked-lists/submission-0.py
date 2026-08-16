# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2

        # Always do edge cases None at the top.
        if not curr1:
            return curr2
        if not curr2:
            return curr1

        # Comparing the value is different than comparing the Node.
        if curr1.val > curr2.val:
            head = curr2
            curr2 = curr2.next
        else: 
            head = curr1
            curr1 = curr1.next

        curr = head

        while (curr1 and curr2):
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next

            curr = curr.next

        while curr1:
            curr.next = curr1
            curr1 = curr1.next
            curr = curr.next
        
        while curr2:
            curr.next = curr2
            curr2 = curr2.next
            curr = curr.next
        
        return head
            

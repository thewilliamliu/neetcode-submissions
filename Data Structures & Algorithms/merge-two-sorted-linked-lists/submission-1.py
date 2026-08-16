# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Instead of doing another if loop to get the head, do a dummy and keep the loop as just one large one.        
        dummy = node = ListNode()

        while (list1 and list2):
            # Comparing the value is different than comparing the Node.
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next

        # Rather than another full while loop, just attach the node that isn't None.
        node.next = list1 or list2

        return dummy.next
            

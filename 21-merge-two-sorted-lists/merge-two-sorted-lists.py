# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a sentinel node as the head of the merged list
        sentinel = ListNode()
        current = sentinel
        
        # Merge the lists while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append the remaining nodes of list1 or list2
        current.next = list1 or list2
        
        # Return the merged list, skipping the sentinel node
        return sentinel.next

        
        # Merge lists while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append remaining nodes of list1 or list2
        current.next = list1 or list2
        
        # Return the head of the merged list
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Ensure list1 starts with the smaller head
        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        # Initialize the head of the merged list
        head = list1
        
        # Traverse both lists to merge them
        while list1.next and list2:
            if list1.next.val > list2.val:
                list1.next, list2 = list2, list1.next
            list1 = list1.next
        
        # Append remaining nodes of list2 to list1
        if list2:
            list1.next = list2
        
        return head


        
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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val > l2.val:
            l1, l2 = l2, l1
        
        head = l1
        while l1 and l2:
            if l1.next and l1.next.val > l2.val:
                l1.next, l2 = l2, l1.next
            elif not l1.next:
                l1.next = l2
                break
            l1 = l1.next
        
        return head


        
        current.next = list2
        
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


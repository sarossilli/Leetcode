# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        
        if l1.val<l2.val:
            head = node = ListNode(l1.val)
            l1=l1.next
        else:
            head = node = ListNode(l2.val)
            l2=l2.next
        
        while(l1 and l2):
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
                
            node = node.next
            
        while(l1):
            node.next = l1
            l1 = l1.next
            node = node.next
            
        while(l2):
            node.next = l2
            l2 = l2.next
            node = node.next
        
        return head
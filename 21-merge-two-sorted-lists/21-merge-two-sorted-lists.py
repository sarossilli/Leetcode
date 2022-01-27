# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val<list2.val:
            head = list1
            cur1 = list1.next
            cur2 = list2
        else:
            head = list2
            cur2 = list2.next
            cur1 = list1
            
        
        cur = head
        while cur1 and cur2:
            if cur1.val>cur2.val:
                cur.next = cur2
                cur2 = cur2.next
            else:
                cur.next = cur1
                cur1 = cur1.next
            cur = cur.next
        
        while cur1 :
            cur.next = cur1
            cur = cur.next
            cur1 = cur1.next
            
        while cur2 :
            cur.next = cur2
            cur = cur.next
            cur2 = cur2.next
        
        return head
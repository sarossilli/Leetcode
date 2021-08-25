# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = cur = ListNode()
        
        
        n1,n2 = l1, l2
        toAdd = 0
        
        while(n1 and n2):
            cur.next = ListNode(n1.val + n2.val + toAdd)
            toAdd = 0
            
            if cur.next.val >= 10:
                val = (cur.next.val%10)
                toAdd = int((cur.next.val - val)/10)
                cur.next.val = val
            n1 = n1.next
            n2 = n2.next
            cur = cur.next
        while(n1):
            cur.next = ListNode(n1.val + 0 + toAdd)
            toAdd = 0
            
            if cur.next.val >= 10:
                val = (cur.next.val%10)
                toAdd = int((cur.next.val - val)/10)
                cur.next.val = val
            n1 = n1.next
            cur = cur.next
        
        while(n2):
            cur.next = ListNode(n2.val + 0 + toAdd)
            toAdd = 0
            
            if cur.next.val >= 10:
                val = (cur.next.val%10)
                toAdd = int((cur.next.val - val)/10)
                cur.next.val = val
            n2 = n2.next
            cur = cur.next
            
        if toAdd:
            cur.next = ListNode(toAdd)
            
        return res.next
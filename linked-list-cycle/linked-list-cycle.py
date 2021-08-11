# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        if slow: #not none
            fast = head.next
        else:
            return False
        
        while(slow and fast and fast.next): #not none
            if (fast == slow):
                return True
            else:
                fast = fast.next.next
                slow = slow.next
        return False
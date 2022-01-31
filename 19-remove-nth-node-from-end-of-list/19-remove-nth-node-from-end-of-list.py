# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Traverse to end, add to stack
# pop off stack times, save the previous one

# 1 2 3 4 5
# [1 2 3 5]
# 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode(0)
        root.next = head
        leftNode = rightNode = root
        
        for i in range(n+1):
            rightNode = rightNode.next
        
        while rightNode:
            rightNode = rightNode.next
            leftNode = leftNode.next
        
        leftNode.next = leftNode.next.next
        
            
            
            
            
        return root.next
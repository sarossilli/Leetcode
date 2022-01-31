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
        stack = []
        curNode = head
        
        while curNode:
            stack.append(curNode)
            curNode = curNode.next
        
    
        stack.pop(len(stack)-n)
        
        if stack:
            root = cur = stack.pop(0)
            
            for k in range(len(stack)):
                cur.next = stack.pop(0)
                cur = cur.next
            cur.next = None
            return root
        
        else:
            return None

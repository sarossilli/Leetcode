# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curNode = head
        while curNode:
            stack.append(curNode)
            curNode = curNode.next
        if not len(stack):
            return head
        
        head = curNode = ListNode(stack.pop(-1).val)
        while len(stack):
            curNode.next = ListNode(stack.pop(-1).val)
            curNode = curNode.next
        return head
            
        
        
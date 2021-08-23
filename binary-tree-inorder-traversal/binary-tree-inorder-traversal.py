# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = deque() # FIFO
        curNode = root
        while stack or curNode: #While not done/empty
            if curNode:
                stack.append(curNode)
                curNode = curNode.left
            else:
                curNode = stack.pop()
                res.append(curNode.val)
                curNode = curNode.right
        
        return res
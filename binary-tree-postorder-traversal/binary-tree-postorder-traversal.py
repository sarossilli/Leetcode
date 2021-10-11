# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return
        q = [root]
        
        while q:
            cur = q.pop()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
                
            res.append(cur.val)
            
            
        while q:
            res.append(cur.val)
            cur = q.pop()
            
        return res[::-1]
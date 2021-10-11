# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = [root,root]
        while len(q):
            n1 = q.pop()
            n2 = q.pop()
            if not n1 and not n2:
                continue
            if (not n1 and n2) or (n1 and not n2):
                return False
            if n1.val != n2.val:
                return False
            
            q.append(n1.left)
            q.append(n2.right)
            q.append(n1.right)
            q.append(n2.left)
        return True
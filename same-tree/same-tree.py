from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        
        if not p and not q:
            return True
        elif not p and q or not q and p:
            return False
        st_1 = deque()
        st_1.append(p)

        
        st_2 = deque()
        st_2.append(q)
        n1,n2 = None, None
        while len(st_1) and len(st_2):
            n1 = st_1.popleft()
            n2 = st_2.popleft()
            
            if n1 and n2 and n1.val != n2.val:
                return False

            
            if n1.left and n2.left:
                st_1.append(n1.left)
                st_2.append(n2.left)
            elif n1.left and not n2.left or n2.left and not n1.left:
                return False
            
            if n1.right and n2.right:
                st_1.append(n1.right)
                st_2.append(n2.right)
            elif n1.right and not n2.right or n2.right and not n1.right:
                return False
            
        if not (len(st_1) or len(st_2)):
            return True
        else:
            print("END ONE NOT EMPTY")
            return False
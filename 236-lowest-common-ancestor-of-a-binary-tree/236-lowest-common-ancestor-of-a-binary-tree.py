# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        
        parent = {root:None}
        # {root:none, 2:root, 4:root, 3:2}
        
        #Break when we find p and q
        while p not in parent or q not in parent:
            
            cur = stack.pop()

            if cur.left:
                parent[cur.left] = cur
                stack.append(cur.left)
            if cur.right:
                parent[cur.right] = cur
                stack.append(cur.right)

        ancestors = set()
        #{p}

        while p:
            ancestors.add(p)
            p = parent[p] #{3}

        while q not in ancestors:
            q = parent[q]
            
        return q
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        m = 0

        def dfs(n,root):
            if not root:
                return n
            
            return max(dfs(n+1,root.left),dfs(n+1,root.right))
        
        m = dfs(m,root)
            
        return m
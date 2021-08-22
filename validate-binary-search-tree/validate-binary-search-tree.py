# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            return dfs(root.left) + [root.val] + dfs(root.right) if root else []
        res = dfs(root)
        
        for i in range(1,len(res)):
            if res[i-1] >= res[i]:
                return False
        return True
                    
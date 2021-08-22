# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Start Recursion
        result = dfs(root)
        
        #check order
        for i in range(len(result)-1):
            if result[i] >= result[i+1]:
                return False
        return True
    
    
def dfs(node):
    result = []
    if node:
        # Left Tree
        if node.left:
            result += dfs(node.left)
            
        # Add value to result list
        result.append(node.val)

        # Right Tree
        if node.right:
            result += dfs(node.right)
            
        return result
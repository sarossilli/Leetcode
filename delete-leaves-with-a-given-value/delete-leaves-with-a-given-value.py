# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def traverse(node):
            if not node:
                return
            node.left=traverse(node.left)
            node.right=traverse(node.right)
            
            if node.val==target and not node.right and not node.left:return None
            return node 
        root = traverse(root)
        return root
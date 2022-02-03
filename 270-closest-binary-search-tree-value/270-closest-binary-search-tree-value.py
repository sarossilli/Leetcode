# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        val = result = root.val
        curNode = root
        while(root):
            val = root.val
            if (abs(val-target) < abs(result-target)):
                result = val
            if target<val:
                root = root.left
            else:
                root = root.right
                
        return result
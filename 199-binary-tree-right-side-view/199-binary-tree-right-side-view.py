# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        rightView = [root.val]
        
        curlevel = list()
        nextLevel = list()
        if root.left:
            nextLevel.append(root.left)
        if root.right:
            nextLevel.append(root.right)

        while len(nextLevel):
            curLevel = nextLevel
            nextLevel = list()
            while len(curLevel):
                item = curLevel.pop(0)
                if item.left:
                    nextLevel.append(item.left)
                if item.right:
                    nextLevel.append(item.right)
            rightView.append(item.val)
        

                    
        
        
        
        return rightView
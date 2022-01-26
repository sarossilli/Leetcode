# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        current = root
        stack = [] 
        result = 0

        while True:

            if current is not None:
                stack.append(current)

                current = current.left

            elif(stack):
                current = stack.pop()
                if(current.val>=low and current.val<=high):
                    result+=current.val

                current = current.right

            else:
                return result

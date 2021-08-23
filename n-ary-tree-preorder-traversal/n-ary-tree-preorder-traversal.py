"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
def recurse(root):
    if not root:
        return []
    res = []
    #res.append(root.val)
    while root.children:
        res += recurse(root.children.pop())       
    res.append(root.val)
    
    return res
    
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        return recurse(root)[::-1]
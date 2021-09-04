# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        
        
        if not root:
            return ""
        
        res = ""
        stack = deque()
        stack.append(root)
        
        while len(stack):
            node = stack.popleft()
            if node:
                res += str(node.val) + ','
                stack.append(node.left)
                stack.append(node.right)
            else:
                res += "null,"

        return res[:-1]
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if data == "":
            return
        
        res = data.split(',')
        if res[0] == 'null':
            return
        else:
            root = TreeNode(int(res[0]))
            
        curNode = root
        stack = deque()
        for i in range(1,len(res)-1,2):
            if res[i] != 'null':
                curNode.left = TreeNode(int(res[i]))
                stack.append(curNode.left)
            if res[i+1] != 'null':
                curNode.right = TreeNode(int(res[i+1]))
                stack.append(curNode.right)
            if len(stack):
                curNode = stack.popleft()
            else:
                break
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
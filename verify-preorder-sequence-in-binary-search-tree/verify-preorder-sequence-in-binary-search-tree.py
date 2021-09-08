class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # r l ri
        
        # 2 1 3 
        
        low = -1*(math.inf)
        stack = []
        
        for cur in preorder:
            if cur < low:
                return False
            
            while stack and cur>stack[-1]:
                low = stack.pop()
                
            stack.append(cur)
            
        return True
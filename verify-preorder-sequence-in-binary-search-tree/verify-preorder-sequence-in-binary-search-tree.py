class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        lower = -1 * math.inf
        
        path = []
        
        for n in preorder:
            if n < lower:
                return False
            while len(path) and n > path[-1]:
                lower = path.pop()
            path.append(n)
            
        return True
        

# [5,2,1,3,6] lb = -inf []
# [2,1,3,6] lb = -inf [5]
# [1,3,6] lb = -inf [5,2]
# [3,6] lb = -inf [5,2,1]
# [6] lb = 1 [5,2,3]
# 
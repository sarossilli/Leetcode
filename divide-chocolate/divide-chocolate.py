# 1 2 3 4 
# max = 11

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        r = sum(sweetness)//(k+1)
        l = min(sweetness)

        while l<r:
            m = (l + r + 1)//2
            cur_s = 0
            p = 0
            
            for s in sweetness:
                cur_s += s
                if cur_s >= m:
                    p+=1
                    cur_s = 0
            
            if p>=k+1:
                l=m
            else:
                r=m-1
        return r
        
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for i in accounts:
            s = 0
            for k in i:
                s+=k
                if s>res:
                    res=s
                    
        return res
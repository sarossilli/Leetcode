class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        l = len(s)
        if l == 1 or numRows == 1:
            return s
        
        inc = 2* numRows - 2
        for i in range(numRows):
            for k in range(0,l,inc):
                if k+i<l:
                    res+=s[k+i] 
                    if i != 0 and i!=numRows-1 and k+inc-i<l:
                        res+=s[k+inc-i]

        return res
        
        # 1 _ 5                 ->4
        
        # 1 _ _  7 _ _ 13       ->6
        
        # 4 _ _ 10              ->
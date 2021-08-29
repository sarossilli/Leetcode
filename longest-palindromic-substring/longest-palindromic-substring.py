def findCenter(s,l,r):
    L,R = l,r
    while(L>=0 and R<len(s) and s[L] == s[R]):
        L-=1
        R+=1
    return R-L-1


class Solution:
    

    
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        start,end = 0,0
        
        for k in range(len(s)):
            len1 = max(findCenter(s,k,k),findCenter(s,k,k+1))
            if len1>end-start:
                start = k - int((len1-1) / 2)
                end = (k + int(len1/2))
            
            print(start,end)
        return s[start:end+1]
        
        
            
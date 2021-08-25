class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        
        ans = 0
        for k in range(len(s)):
            seen = set()
            res = 0
            for i in range(k,len(s)):
                if s[i] in seen:
                    if res > ans:
                        ans = res
                    break
                else:
                    seen.add(s[i])
                    res += 1
        
            if res > ans:
                ans = res                    
                
        
        return ans
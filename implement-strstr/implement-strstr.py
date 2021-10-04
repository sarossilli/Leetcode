class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        if not n_len:
            return 0
        
        i = 0
        while(i<len(haystack)):
            if haystack[i:i+n_len] == needle:
                return i
            i+=1
        return -1
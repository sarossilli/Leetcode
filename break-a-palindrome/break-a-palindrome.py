# A A A
# A A B

# B C C B
# A B C B

# A A C C B A

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        
        res = ""
        indx = 0
        found = False
        
        while not found and indx <= int(len(palindrome)/2)-1:
            if ord(palindrome[indx]) > ord("a"):
                res += 'a'
                print((palindrome[indx]), "FOUND")
                found = True
            else:
                res += palindrome[indx]
            
            indx += 1
            
        while indx < len(palindrome):
            res += palindrome[indx]
            indx += 1
            
        if not found:
            res = res[:-1]
            res += 'b'
            
        return res
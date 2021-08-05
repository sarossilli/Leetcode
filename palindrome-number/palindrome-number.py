class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        x = str(x)
        for i, value in enumerate(x):
            comp = len(x)-i-1
            if value != x[comp]:
                return False
        return True
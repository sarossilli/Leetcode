class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        
        left, right = 2, x // 2
        
        while left <= right:
            guess = left + (right - left) // 2
            num = guess * guess
            if num > x:
                right = guess - 1
            elif num < x:
                left = guess + 1
            else:
                return guess
        return right
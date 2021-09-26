# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 0,n
        while l<r:
            m = int(l + (r-l)/2)
            g = guess(m)
            if g == 0:
                return m
            elif g<0:
                r = m
            else:
                l = m+1
        return l
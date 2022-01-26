class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                rmL = list(s)
                rmR = list(s)

                rmL.pop(l)
                rmR.pop(r)

                if rmL == rmL[::-1] or rmR == rmR[::-1]:
                    return True

                return False

            l += 1
            r -= 1
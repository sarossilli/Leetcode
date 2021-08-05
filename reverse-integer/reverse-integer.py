class Solution:
    def reverse(self, x: int) -> int:
        digits = [(i) for i in str(x)]
        isNeg = False
        if digits[0] == '-':
            digits = digits[1:]
            isNeg = True
        
        digits = int("".join(digits[::-1]))
        if digits > pow(2,31):
            return 0
        else:
            if isNeg:
                return (0-digits)
            else:
                return digits
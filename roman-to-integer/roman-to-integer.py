class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        prev = ''
        for char in s:
            if char == 'I':
                res +=1
            elif char == 'V':
                if prev == 'I':
                    res += 3
                else:
                    res +=5
            elif char == 'X':
                if prev == 'I':
                    res +=8
                else:
                    res +=10
            elif char == 'L':
                if prev == 'X':
                    res += 30
                else:
                    res += 50
            elif char == 'C':
                if prev == 'X':
                    res += 80
                else:
                    res += 100
            elif char == 'D':
                if prev == 'C':
                    res += 300
                else:
                    res += 500
            elif char == 'M':
                if prev == 'C':
                    res += 800
                else:
                    res += 1000
            prev = char
        return res
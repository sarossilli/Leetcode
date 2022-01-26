class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        n = max(len(num1),len(num2))
        res = list()
        carry = 0
        for i in range(n):
            r = 0
            if i<len(num1) and i <len(num2):
                c1 = ord(num1[i])-48
                c2 = ord(num2[i])-48
                r= (c1+c2+carry)
                if r>9:
                    carry = r//10
                    r = r%10
                else:
                    carry = 0
                res.append(chr(r+48))
            elif i<len(num1):
                c1 = ord(num1[i])-48
                r= (c1+carry)
                if r>9:
                    carry = r//10
                    r = r%10
                else:
                    carry = 0
                res.append(chr(r+48))
            elif i<len(num2):
                c1 = ord(num2[i])-48
                r= (c1+carry)
                if r>9:
                    carry = r//10
                    r = r%10
                else:
                    carry = 0
                res.append(chr(r+48))
            
        if carry>0:
            res.append(chr(carry+48))
        return "".join(res[::-1])
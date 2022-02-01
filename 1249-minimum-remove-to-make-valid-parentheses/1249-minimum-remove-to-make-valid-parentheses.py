# "balance" -> amt of open/close <0 need opening


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        bal = 0
        result = ""
        for c in s:
            if c == '(':
                bal+=1
            elif c == ')':
                if bal==0:
                    continue
                bal-=1
            result+=c
                
        bal=0
        s=result
        result = ""

        for c in s[::-1]:
            if c == ')':
                bal+=1
            elif c == '(':
                if bal==0:
                    continue
                bal-=1
            result+=c
                   
        return result[::-1]
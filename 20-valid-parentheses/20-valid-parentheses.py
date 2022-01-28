class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        #{()}]
        for c in s:
            if c == '{' or c == '(' or c == '[':
                stack.append(c)
            else:
                if not len(stack):
                    return False
                
                r = stack.pop(-1)
                if c==')' and r != '(':
                    return False
                elif c=='}' and r != '{':
                    return False
                elif c==']' and r != '[':
                    return False
                
        if stack:
            return False
        return True
                
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        for i, char in enumerate(s[1:]):
            if char == ")" or char == "]" or char == "}":
                if len(stack)==0:
                    return False
                prev = stack.pop()
                if char == ")":
                    if prev != "(":
                        return False
                if char == "]":
                    if prev != '[':
                        return False
                if char == "}":
                    if prev != '{':
                        return False
            else:
                stack.append(char)

        return not len(stack)
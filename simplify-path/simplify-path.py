class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = list()
        for s in path:
            if s == "" or s == ".":
                continue
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return "/" + "/".join(stack)
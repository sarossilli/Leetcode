class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        ans = ""
        for i in range(len(strs[0])):
            prev = strs[0][0:i+1]

            for string in strs[1:]:
                if string[0:i+1] != prev:
                    return prev[0:-1]
                else:
                    ans = prev
        return ans
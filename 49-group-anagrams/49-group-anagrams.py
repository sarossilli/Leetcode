class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        for w in strs:
            count = [0]*26
            for c in w:
                count[ord(c)-ord('a')] += 1
            hashVal = tuple(count)
            if hashVal in ans:
                ans[hashVal].append(w)
            else:
                ans[hashVal] = [w]
        return ans.values()
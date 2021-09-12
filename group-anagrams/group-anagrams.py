# {e,a,t}
# {t,e,a}

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key = {}
        for i, s in enumerate(strs):
            letter = "".join(sorted(s))
            if letter in key:
                key[letter].append(s)
            else:
                key[letter] = [s]

        res = [k for k in key.values()]
        return res
        
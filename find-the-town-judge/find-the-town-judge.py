class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_count = [0]*n #o(N) Space
        out_count = [0]*n
        
        for a_trusts, b in trust: #O(N)
            in_count[b-1] +=1
            out_count[a_trusts-1] += 1

        max_seen = 0
        for person, count in enumerate(out_count):
            if count == 0 and in_count[person] == n-1:
                return person+1
            
        return -1
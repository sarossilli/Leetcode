class Solution:
    def rob(self, nums: List[int]) -> int:

        r1,r2 = 0,0
        
        for i in nums:
            res = max(r1 + i, r2)
            r1 = r2
            r2 = res
        
        return r2
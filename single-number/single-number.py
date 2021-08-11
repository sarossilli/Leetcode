class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        seen = dict()
        for i in nums:
            if i in seen:
                seen[i] +=1
            else:
                seen[i] = 1
        
        for i in seen:
            if seen[i] == 1:
                return i
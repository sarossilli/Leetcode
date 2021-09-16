class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        looking_for = dict()
        
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in looking_for:
                return [i, looking_for[comp]]
            
            looking_for[nums[i]] = i
            
        
        
# [2,7,11,15]  9


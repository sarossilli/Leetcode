class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        cur_sum = cur_max = nums[0]
        
        for k in nums[1:]:
            cur_sum = max(k,cur_sum+k)
            cur_max = max(cur_sum,cur_max)
            
        return cur_max
    
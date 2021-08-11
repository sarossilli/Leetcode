class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            n ^= i
            n ^= nums[i]
        return n
    

# 1 0 0 
# 0 0 0 i = 0
# 1 0 1 
# 1 0 0
# 0 0 1 i = 1
# 0 0 1
# 0 0 0 i = 2
# 0 1 0
# 0 1 0

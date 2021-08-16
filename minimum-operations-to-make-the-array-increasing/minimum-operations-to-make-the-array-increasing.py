class Solution:
    def minOperations(self, nums: List[int]) -> int:
        last = 0
        output = 0
        for i in range(len(nums)):
            if last>=nums[i]:
                output += ((last+1)-nums[i])
                nums[i] = last+1
            last = nums[i]
        return output
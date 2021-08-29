class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 0
        for j in range(len(nums)):
            if nums[j] != nums[n]:
                n+=1
                nums[n] = nums[j]
        return n+1
                
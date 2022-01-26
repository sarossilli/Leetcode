# [3,2,2,3]

# [3,2,2,_]
# [3,2,2,_]
# [3,2,2,_]
# [2,2,2,_]
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==val:
                nums[i:] = nums[i+1:]
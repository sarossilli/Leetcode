class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()
        
        for i in range(len(nums)):
            
            if i==0 or nums[i] != nums[i-1]:
                self.twoSum(nums,i,res)
        
        return res
    
    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        l, r = i + 1, len(nums) - 1
        
        while (l < r):
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
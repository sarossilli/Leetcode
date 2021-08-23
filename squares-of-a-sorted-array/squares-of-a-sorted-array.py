class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not len(nums):
            return
        elif len(nums) == 1:
            return [nums[0]**2]
        
        res = []
        cur = nums[0]
        r = 0
        
        while cur<0 and r<len(nums)-1:
            r+=1
            cur = nums[r]
            
        l = r-1
            
        
        while r<len(nums) and l>=0:
            if nums[r]<abs(nums[l]):
                res.append(nums[r]**2)
                r+=1
            else:
                res.append(nums[l]**2)
                l-=1
        
        while l>=0:
            res.append(nums[l]**2)
            l-=1
        while r<len(nums):
            res.append(nums[r]**2)
            r+=1
            
        

        return res
        
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxPair = -1*math.inf
        l,r = 0,len(nums)-1
        
        while (l<r):
            res = nums[l] + nums[r]
            if res > maxPair:
                maxPair = res
            l+=1
            r-=1
        return maxPair
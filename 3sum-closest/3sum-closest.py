class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        curMin = math.inf

        for i in range(len(nums)):
            l,r = i+1 ,  len(nums)-1
            while(l<r):
                s = nums[i] + nums[l] + nums[r]
                if abs(target-s) < abs(curMin):
                    curMin = target-s
                    
                if s<target:
                    l+=1
                else:
                    r-=1
            if curMin == 0:
                break
        return target-curMin
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        degree = 0
        maxSeenSet = set()
        l,count, r = dict(),dict(),dict()
        
        
        for k, i in enumerate(nums):
            if i in count:
                count[i] += 1
                r[i] = k 
            else:
                count[i] = 1
                l[i] = k 
                r[i] = k 
            
            if count[i]>degree:
                degree = count[i]
                maxSeenSet = set()
                maxSeenSet.add(i)
                
            elif count[i] == degree:
                maxSeenSet.add(i)
        
        minSize = len(nums)
        for i in maxSeenSet:
            if r[i] - l[i] < minSize:
                minSize = r[i] - l[i]
        
        return minSize+1

        
# [1,2,2,3,1]

# {1: 0} {1: 2} {1: 4}
# {2: 1} {1: 2} {1: 2}
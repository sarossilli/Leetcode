class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = dict()
        n = len(nums)
        for i in nums:
            if i in count:
                count[i] +=1 
            else:
                count[i] = 1
        ans = -1
        for i in count.keys():
            if count[i] > int(n/2):
                return i
            
# 2 2 1 2 1 1 1
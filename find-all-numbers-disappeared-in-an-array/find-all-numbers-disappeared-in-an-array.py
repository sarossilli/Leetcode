class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [-1 for i in range(1,len(nums)+1)]
        ans = []
        for val in nums:
            arr[val-1] = val-1
        
        for i,val in enumerate(arr):
            if val < 0:
                ans.append(i+1)
        
        return ans
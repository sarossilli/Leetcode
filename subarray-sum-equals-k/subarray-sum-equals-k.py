class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = summ = 0
        dic = dict()
        dic.setdefault(0)
        dic[0] = 1
        
        for i in range(len(nums)):
            summ += nums[i]
            if summ-k in dic:
                ans += dic[summ-k]
                
            if summ in dic:
                dic[summ] += 1
            else:
                dic[summ] = 1
                
                
        return ans
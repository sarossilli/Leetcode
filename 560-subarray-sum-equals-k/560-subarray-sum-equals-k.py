# 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq_dict={0:1}
        
        count=sum_now=0
        for num in nums:
            sum_now += num
            count += freq_dict.get((sum_now-k),0) 
            freq_dict[sum_now] = freq_dict.get(sum_now,0)+1
        
        return(count)
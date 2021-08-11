class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums) #A bunch of 1s
        
        #forward pass
        pre = 1
        for i in range(len(nums)):
            answer[i] = pre
            pre *= nums[i]
        
        #backward pass
        post = nums[-1]
        j = len(nums)-2
        while j >= 0:
            answer[j] *= post
            post *= nums[j]
            j -= 1
        
        return answer
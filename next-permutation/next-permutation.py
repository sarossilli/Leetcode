#Input: nums = [1,2,3]
# 3
# 2 is decreasing, find first bigger, 3
# swap 2 and 3

#Input: nums = [3,2,1]
# 1
# 2
# 3
# return sorted(nums)

#Input: nums = [3,3,1]
# 1
# 3
# 3
# return sorted(nums)

#Input: nums = [2,3,1]
# 1
# 3
# 2 is decreased, first bigger is 3
# swap 3 and 2
# return sorted(nums)


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        
        l = len(nums)-2
        prev = nums[-1]
        while l>=0 and nums[l] >= nums[l+1]:
            l-=1
            
        if l>=0:
            j = len(nums)-1
            while nums[l] >= nums[j]:
                j-=1
                
            tmp = nums[j]
            nums[j] = nums[l]
            nums[l] = tmp
            
        i = l + 1
        k = len(nums)-1
        while i<k:
            tmp = nums[k]
            nums[k] = nums[i]
            nums[i] = tmp
            i+=1
            k-=1
            
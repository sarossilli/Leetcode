class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        
        for val in nums:
            if val in seen:
                return True
            else:
                seen.update({val:1})
                
        return False
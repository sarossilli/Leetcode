class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-k for k in nums]
        h = heapq.heapify(nums)
        for n in range(k):
            r = heapq.heappop(nums)
            
        return -r
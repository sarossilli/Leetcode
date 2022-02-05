class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        lowest = math.inf
        for k in prices:
            maximum = max(maximum,k-lowest)
            lowest = min(lowest,k)
        return maximum
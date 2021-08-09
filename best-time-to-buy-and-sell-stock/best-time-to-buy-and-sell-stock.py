class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1
        ans = 0
        while(right < len(prices)):
            if prices[left] < prices[right]:
                prof = prices[right] - prices[left]
                ans = max(ans,prof)
            else:
                left=right
            right+=1
        return ans
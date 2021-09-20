class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        curMax = 0
        while(l<r):
            if height[r]<height[l]:
                curWater =height[r]*(r-l)
                r-=1
            else:
                curWater =height[l]*(r-l)
                l+=1
            curMax = max(curMax,curWater)
            
        return curMax
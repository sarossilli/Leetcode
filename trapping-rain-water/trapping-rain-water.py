#0,2 - min0,1 0
#1,3 - min1,2 1->1*1 = 1
#3,5 - min2,1 ->1
#3,6 - 
#3,7 - min2,3 ->2*3 = 6 - 2

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2:
            return 0
        
        ans = 0

        max_l = [0]*len(height)
        max_l[0] = [height[0]]
        
        for i,val in enumerate(height):
            max_l[i] = (max(max_l[i-1],val))
            
        max_r = [0]*len(height)
        max_r[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            max_r[i] = (max(max_r[i+1],height[i]))
            

        for i in range(len(height)):
            ans += min(max_l[i],max_r[i]) - height[i]
            
        
        return ans
    
class Solution:
    def climbStairs(self, n: int) -> int:
        steps = {'1':1,'2':2}
        
        for i in range(3,n+1):
            steps[str(i)] = steps[str(i-1)] + steps[str(i-2)]
        return steps[str(n)]
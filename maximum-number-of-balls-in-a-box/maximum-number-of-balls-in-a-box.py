class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        balls = [sum(int(d) for d in str(i)) for i in range(lowLimit,highLimit+1)]
        print(balls)
        dic = {}
        ans = 1
        
        for each in balls:
            if each in dic:
                dic[each] += 1
                if dic[each]>ans:
                    ans = dic[each]
            else:
                dic.update({each:1})
            
        return ans 
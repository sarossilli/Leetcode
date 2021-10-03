class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
            
        count = dict()
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        
        n = sorted(count.items(),key= lambda x: (x[1],-x[0]))
        res = []
        
        for k,c in n:
            for i in range(c):
                res.append(k)
                
        return res
from collections import OrderedDict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = OrderedDict()
        for i in nums:
            if i in a:
                a[i] +=1
            else:
                a[i] = 1
        
        a = sorted(a.items(),key=lambda t: t[1], reverse=True)
        a = [k for k,v in a[0:k]]
        return (a)
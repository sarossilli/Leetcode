

 

class Solution:
    def mergeIntervals(self, arr):
        arr.sort(key = lambda x: x[0])
        m = []
        s = -10000
        max = -100000
        for i in range(len(arr)):
            a = arr[i]
            if a[0] > max:
                if i != 0:
                    m.append([s,max])
                max = a[1]
                s = a[0]
            else:
                if a[1] >= max:
                    max = a[1]
        
        if max != -100000 and [s, max] not in m:
            m.append([s, max])
        
        return m
    
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = dict()
        for i,val in enumerate(s):
            if val not in lastIndex:
                lastIndex[val] = [i,i]
            else: 
                lastIndex[val] = [lastIndex[val][0],i]
        arr = [i[1] for i in lastIndex.items()]
        arr = self.mergeIntervals(arr)
        res = []
        for i in range(len(arr)-1):
            res.append(arr[i+1][0] - arr[i][0])
        
        res.append(len(s) - arr[-1][0])
        return res
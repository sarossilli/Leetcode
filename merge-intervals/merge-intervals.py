class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort
        intervals.sort(key = lambda x: x[0])
        merged = []
        for interval in intervals:
            if merged and merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1],interval[1])
            else:
                merged.append(interval)
        return merged       
    
#[[1,3],[2,6],[8,10],[15,18]]
# L = 1, h = 3
# 1<2<3 SO MERGE? -> [1,6]
# L = 1 H = 6
# 1<6<8 SO NO MERGE
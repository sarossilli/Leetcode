from collections import OrderedDict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lengths = []
        
        for i in points:
            dist = sqrt(i[0]**2 + i[1]**2)
            lengths.append([dist,i])
        
        lengths.sort()
        lengths = [i[1] for i in lengths[:k]]
        return lengths
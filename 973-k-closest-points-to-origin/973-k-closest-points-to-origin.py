class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        indexRank = list()
        for indx,p1 in enumerate(points):
            dist = p1[0]**2 + p1[1]**2
            indexRank.append((dist,indx))
        indexRank.sort(key= lambda x: x[0])
        indexRank = indexRank[:k]
        result = [points[indx[1]] for indx in indexRank]
        return result
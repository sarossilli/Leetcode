from heapq import heappop, heappush, heappushpop
class MedianFinder:

    def __init__(self):
        self.l = [] #maxheap
        self.r = []
        self.m = 0
        
    def addNum(self, num: int) -> None:
        if len(self.l) == len(self.r):
            heappush(self.l, -heappushpop(self.r, -num))
        else:
            heappush(self.r, -heappushpop(self.l, num))

            
    def findMedian(self) -> float:
        if len(self.l) != len(self.r):
            return self.l[0]
        else:
            return (self.l[0] + -1*self.r[0])/2
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
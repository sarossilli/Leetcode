class MovingAverage:

    def __init__(self, size: int):
        self.arr = list()
        self.n=0
        self.size = size
        return None
        

    def next(self, val: int) -> float:
        self.arr.append(val)
        if self.n+1>self.size:
            self.arr.pop(0)
        else:
            self.n+=1
        return sum(self.arr)/self.n
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
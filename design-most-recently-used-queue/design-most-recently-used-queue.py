class MRUQueue:

    def __init__(self, n: int):
        self.q = [x for x in range(1,n+1)]
        

    def fetch(self, k: int) -> int:
        self.q = self.q[:k-1] + self.q[k:] + [self.q[k-1]]
        return self.q[-1]


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
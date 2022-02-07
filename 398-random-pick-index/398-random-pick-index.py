class Solution:

    def __init__(self, nums: List[int]):
        self.index = {}
        for i, n in enumerate(nums):
            if n in self.index:
                (self.index[n]).append(i)
            else:
                self.index[n] = [i]
        
    def pick(self, target: int) -> int:
        i = self.index[target]
        val = random.randint(0,len(i)-1)
        return i[val]
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
class LRUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.lru = list()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.data:
            self.lru.remove(key)
            self.lru.insert(0,key)
            return self.data[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data[key] = value
            self.lru.remove(key)
            self.lru.insert(0,key)
        elif len(self.data) == self.cap:
            toRm = self.lru.pop(-1)
            del self.data[toRm]
            self.data[key] = value
            self.lru.insert(0,key)
        else:
            self.data[key] = value
            self.lru.insert(0,key)
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

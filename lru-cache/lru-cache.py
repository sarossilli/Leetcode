class DLinkedNode(): 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
        
class LRUCache:
    def _add_node(self,node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        
    def _remove_node(self,node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev
        
    def _addFront(self,node):
        self._remove_node(node)
        self._add_node(node)
        
    def _popEnd(self):
        res = self.tail.prev
        self._remove_node(res)
        return res
    
    def __init__(self, capacity: int):
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lru = dict()
        self.size = 0
        self.cap = capacity

        
    def get(self, key: int) -> int:
        node = self.lru.get(key,None)
        if node:
            self._addFront(node)
            return node.value
        else:
            return -1
        
        
    
    def put(self, key: int, value: int) -> None:
        node = self.lru.get(key,None)
        if node:
            node.value = value
            self._addFront(node)
        else:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value
            self.lru[key] = newNode
            self._add_node(newNode)
            self.size +=1
            
            if self.size > self.cap:
                tail = self._popEnd()
                del self.lru[tail.key]
                self.size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

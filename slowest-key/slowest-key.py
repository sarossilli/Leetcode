class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans = prev = 0
        key = 0
        
        for k,val in enumerate(releaseTimes):
            a = val - prev
            print(a,keysPressed[k])
            if a > ans or (a==ans and ord(keysPressed[key]) < ord(keysPressed[k])):
                ans = a
                key = k
            prev = val
                
        return keysPressed[key]
                
            
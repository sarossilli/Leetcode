from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        d = {1: '', 2: 'abc',3: 'def',4: 'ghi',5: 'jkl',6: 'mno',7: 'pqrs',8: 'tuv',9: 'wxyz'}
        q = deque(d[int(digits[0])])
        #[abc]
        
        for i in range(1,len(digits)):
            length = len(q)
            while length: #still stuff in queue
                out = q.popleft() #pop permultations
                for j in d[int(digits[i])]: #for each letter in this digit
                    q.append(out + j) #append that letter
                length -= 1
                
        return q
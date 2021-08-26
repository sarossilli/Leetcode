class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = dict()
        for i, k in enumerate(order):
            dic[k] = i
        
        prev = words[0]
        for i in words[1:]:
            print(i,prev)
            indx = 0
            
            while indx < len(prev) and indx < len(i):
                if dic[prev[indx]] > dic[i[indx]]:
                    return False
                elif dic[prev[indx]] == dic[i[indx]]:
                    indx+=1
                else:
                    break
            if indx < len(prev) and indx >= len(i):
                return False
    
            prev = i
        return True
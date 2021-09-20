
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = dict()
        top = []
        def sorter(word):
            # Since highest marks first, least error = most marks
            num = -word[1]
            lex = word[0]
            return (num, lex)

        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        
        top = [w for w,v in sorted(freq.items(),key = sorter)]
            
        return top[:k]
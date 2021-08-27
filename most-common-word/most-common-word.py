class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = {}
        paragraph = paragraph.lower()
        # Removing punctuations in string
        # Using loop + punctuation string
        for ele in paragraph:
            if ele in string.punctuation:
                paragraph = paragraph.replace(ele, " ")
        paragraph = paragraph.split()

        print(paragraph)
        for word in paragraph:
            if "!?',;." in word:
                word = word.replace("!",'')
                
            if word not in banned:
                if word in count:
                    count[word]+=1
                else:
                    count[word]=1

        res = 0
        ans = 0
        for k in count.keys():
            
            if count[k]>res:
                ans = k
                res = count[k]
        
        return ans
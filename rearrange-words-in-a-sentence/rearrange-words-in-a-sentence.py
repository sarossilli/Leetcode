class Solution:
    def arrangeWords(self, text: str) -> str:
        arr = text.split()
        arr = sorted(arr, key=len)
        ans =  " ".join(arr).lower().capitalize() 
        return ans
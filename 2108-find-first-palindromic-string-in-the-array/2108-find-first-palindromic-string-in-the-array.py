class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            pal = True
            i, j = 0, len(word) - 1
            while i < j:
                if word[i] != word[j]:
                    pal = False
                i += 1
                j -= 1
            if pal:   
                return word
        return ""


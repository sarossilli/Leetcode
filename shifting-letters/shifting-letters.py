class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = ""
        shift = sum(shifts) % 26 #total shifts
        
        for i, letter in enumerate(s):
            letter_index = ord(letter) - ord('a') #convert to 0-25
            shifted_letter = chr(ord('a') + (letter_index + shift)%26) #Shift letter
            res += shifted_letter
            shift = (shift - shifts[i])%26 #remove old shift
        
        return res
            
        
        
                
                
                
                
            
            

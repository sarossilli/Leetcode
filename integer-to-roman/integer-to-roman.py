class Solution:
    def intToRoman(self, num: int) -> str:
        
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]

        res = []
        for i,letter in digits:
            if num == 0:
                break
            
            count = num//i
            num = num%i
            
            res.append(letter * count)
            
            
        
        return "".join(res)
    
    
    #101
    # c:1, r=1
    # I
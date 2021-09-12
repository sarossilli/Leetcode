class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = digits[-1]+1
        digits[-1] = k%10
        
        i = len(digits) - 2
        
        while(k//10 > 0 and i>=0):
            k =  (digits[i] +  k//10) #1
            digits[i] = k%10
            i-=1
            
        
        if k // 10 > 0:
            digits.insert(0,(k%10)+1)
        
        return digits
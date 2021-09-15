class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        l, r = 0,(len(palindrome)//2)
        str_arr = [i for i in palindrome]
        
        while l<r:
            if str_arr[l] != "a":
                str_arr[l] = "a"
                return "".join(str_arr)
            l+=1
            
        str_arr[-1] = "b"
        return "".join(str_arr)

            
        
            
            
    

    
    
# A B C C A
# ^       ^

# A B C C A
#   ^   ^    B != c, B < C so turn R down

# A B C B A
#   ^   ^    B != c, turn R down()



# A F C B A
# ^       ^

# A F C C A
#   ^   ^    F != C,  F>C so turn L down

# A B C B A
#   ^   ^    B != c, turn L down()


# A A A A B 
# ^       ^   A != B,  A<B so turn L down

# A F C C A
#   ^   ^    F != C,  F>C so turn L down

# A B C B A
#   ^   ^    B != c, turn L down()

# r^
# Lv
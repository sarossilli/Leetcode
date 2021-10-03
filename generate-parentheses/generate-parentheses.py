class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        
                        
        def valid(A):
            b = 0
            for i in A:
                if i=='(':
                    b+=1
                else:
                    b-=1
                if b<0:
                    return False
            return b==0
            
        def generate(A):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append("(")
                generate(A)
                A.pop()
                A.append(")")
                generate(A)
                A.pop()


        generate([])
        return ans
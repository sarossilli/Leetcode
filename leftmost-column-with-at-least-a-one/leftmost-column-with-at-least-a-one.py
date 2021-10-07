# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        r,c = binaryMatrix.dimensions()
        c_cur = c-1
        r_cur = 0
        
        v = 1
        while(c_cur>=0 and r_cur<r):
            v = binaryMatrix.get(r_cur,c_cur)
            if v==1:
                c_cur -= 1
            else:
                r_cur += 1
        
        return c_cur + 1 if c_cur != c - 1 else -1
        
        
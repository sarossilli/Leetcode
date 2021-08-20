class Solution:
    def traverse(self, grid,i,k,row,col):
        grid[i][k] = 0
        
        #right
        if k<col-1 and grid[i][k+1] == '1':
            self.traverse(grid,i,k+1,row,col)
        
        #left
        if k>0 and grid[i][k-1] == '1':
            self.traverse(grid,i,k-1,row,col)
    
        #up
        if i>0 and grid[i-1][k] == '1':
            self.traverse(grid,i-1,k,row,col)
        
        #Down
        if i<row-1 and grid[i+1][k] == '1':
            self.traverse(grid,i+1,k,row,col)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for k in range(n):
                if grid[i][k] == '1':
                    ans+=1
                    self.traverse(grid,i,k,m,n)
        return ans
    

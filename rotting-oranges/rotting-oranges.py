from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        
        #build set:
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1
        
        queue.append((-1,-1)) #end of queue
        minutes = -1
        
        dirrections = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row,col = queue.popleft()
            if row == -1:
                # Next row in tree
                minutes +=1 
                if queue:
                    queue.append((-1,-1))
            else:
                for d in dirrections:
                    #check around rotten
                    nRow, nCol = row + d[0], col + d[1]
                    #if in range
                    if ROWS > nRow >= 0 and COLS > nCol >= 0:
                        if grid[nRow][nCol] == 1:
                            grid[nRow][nCol] = 2
                            fresh -= 1
                            queue.append((nRow,nCol))
        
        if fresh:
            return -1
        else:
            return minutes
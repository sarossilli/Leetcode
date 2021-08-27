class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visted = [0] * len(isConnected)
        
        def dfs(isConnected,visited,i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(isConnected,visted,j)
        
        for k in range(len(isConnected)):
            if visted[k] == 0:
                dfs(isConnected,visted,k)
                res+=1
                
        return res
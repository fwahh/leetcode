from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = n
        # visit all of the possible cities
        for i in range(n):
            provinces -= self.get_neighbors(i, n, isConnected)
        return provinces
    
    def get_neighbors(self, i, n, isConnected):
        to_explore = {i}
        neighbors = 0
        visited = set()
        while to_explore:
            cur = to_explore.pop()
            isConnected[cur][cur] = 0
            for j in range(n):
                if isConnected[cur][j]:
                    if  j not in visited:
                        neighbors += 1
                        to_explore.add(j)
                        visited.add(j)
                    # change the values when explored to avoid re-exploring
                    isConnected[cur][j] = 0
                    isConnected[j][cur] = 0
                    
        return neighbors
        
isConnected = [[1,1,1],[1,1,1],[1,1,1]]
print(Solution().findCircleNum(isConnected))

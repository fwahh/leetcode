from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        to_transform = []
        # find rotting oranges
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    to_transform.append((i, j))
        time = 0
        while to_transform:
            new_transform = set()
            for i, j in to_transform:
                grid[i][j] = 2
                if i - 1 >= 0 and grid[i - 1][j] == 1 and (i - 1, j) not in to_transform:
                    new_transform.add((i - 1, j))
                if i + 1 < r and grid[i + 1][j] == 1 and (i + 1, j) not in to_transform:
                    new_transform.add((i + 1, j))
                if j - 1 >= 0 and grid[i][j - 1] == 1 and (i, j - 1) not in to_transform:
                    new_transform.add((i, j - 1))
                if j + 1 < c and grid[i][j + 1] == 1 and (i, j + 1) not in to_transform:
                    new_transform.add((i, j + 1))
            if new_transform:
                time += 1
                to_transform = list(new_transform)
            else:
                to_transform = []
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    return -1
        return time
    
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))  # 4

grid = [[2,1,1],[0,1,1],[1,0,1]] 
print(Solution().orangesRotting(grid)) # -1

grid = [[0,2]]
print(Solution().orangesRotting(grid)) # 0

grid = [[1],[1],[1],[1]]
print(Solution().orangesRotting(grid)) # -1

grid = [[2,2],[1,1],[0,0],[2,0]] 
print(Solution().orangesRotting(grid)) # 1
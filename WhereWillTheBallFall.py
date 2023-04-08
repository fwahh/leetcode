class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        R, C  = len(grid), len(grid[0])
        # with memoization
        cache = {}
        def has_path(c: int) -> tuple:
            path = []
            # the ball always moves down if a path exists so max r iterations
            for r in range(R):
                path.append((r, c))
                if (r, c) in cache:
                    return cache[(r, c)], path
                
                if grid[r][c] == 1:
                    if c == C - 1 or grid [r][c + 1] == -1:
                        return -1, path
                    c += 1
                elif grid[r][c] == - 1:
                    if c == 0 or grid[r][c - 1] == 1:
                        return -1, path
                    c -= 1
            return c, path
        res = []
        for j in range(C):
            c, path = has_path(j)
            for tup in path:
                cache[tup] = c
            res.append(c)
        return res
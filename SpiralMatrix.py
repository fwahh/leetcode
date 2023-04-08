from typing import List
from math import ceil

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        R, C = len(matrix), len(matrix[0])
        lim = ceil(min(R, C) / 2)
        r_start = c_start = r = 0
        r_end = R - 1
        c_end = C - 1
        
        for _ in range(lim):
            for c in range(c_start, c_end + 1):
                # print(f"Step 1: r = {r} c={c}")
                res.append(matrix[r][c])
            c_end -= 1
            
            r_start += 1
            for r in range(r_start, r_end + 1):
                # print(f"Step 2: r = {r} c={c}")
                res.append(matrix[r][c])
            
            for c in range(c_end, c_start - 1, -1):
                # print(f"Step 3: r = {r} c={c}")
                res.append(matrix[r][c])
            c_start += 1
            
            r_end -= 1
            for r in range(r_end, r_start - 1, -1):
                # print(f"Step 4: r = {r} c={c}")
                res.append(matrix[r][c])
        
        return res[:R*C]
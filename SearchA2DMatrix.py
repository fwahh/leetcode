from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start = 0
        end = m * n - 1
        while start <= end:
            mid = (start + end)//2
            i, j = divmod(mid, n)
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [1] * n
        for row in range(m - 2, -1, -1):
            curRow = [1] * n 
            for col in range(n - 2, -1, -1):
                curRow[col] = curRow[col + 1] + prevRow[col]
            prevRow = curRow
        return prevRow[0]
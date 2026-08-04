class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            row_prefix = 0
            for c in range(COLS):
                row_prefix += matrix[r][c]
                self.prefix[r][c] = row_prefix
                self.prefix[r][c] += self.prefix[r-1][c] if r - 1 >= 0 else 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        preRB = self.prefix[row2][col2]
        preRT = self.prefix[row1-1][col2] if row1 - 1 >= 0 else 0
        preLB = self.prefix[row2][col1 - 1] if col1 - 1 >= 0 else 0
        preLT = self.prefix[row1-1][col1-1] if (row1 - 1 >= 0 and col1 - 1 >= 0) else 0
        return preRB - preRT - preLB + preLT


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
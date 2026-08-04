class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = matrix
        for r in range(len(self.prefix)):
            total = 0
            for c in range(len(self.prefix[0])):
                total += self.prefix[r][c]
                self.prefix[r][c] = total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2 + 1):
            preRight = self.prefix[r][col2]
            preLeft = self.prefix[r][col1 - 1] if col1 - 1 >= 0 else 0
            total += (preRight - preLeft)
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
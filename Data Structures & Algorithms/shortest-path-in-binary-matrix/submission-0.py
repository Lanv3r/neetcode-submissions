class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        q = deque([(0, 0)])
        path = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return path
                grid[r][c] = 1
                neighbors = [(r - 1, c - 1), (r + 1, c + 1), (r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c - 1), (r - 1, c + 1)]
                for row, col in neighbors:
                    if row in range(rows) and col in range(cols) and grid[row][col] == 0:
                        q.append((row, col))
                        grid[row][col] = 1  
            path += 1  

        return -1 
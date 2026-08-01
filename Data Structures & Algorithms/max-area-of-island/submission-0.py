class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def bfs(i, j):
            visited.add((i, j))
            q = deque([(i, j)])
            size = 0
            while q:
                size += 1
                r, c = q.popleft()
                neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for row, col in neighbors:
                    if (row in range(rows) and
                    col in range(cols) and
                    grid[row][col] == 1 and
                    (row, col) not in visited):
                        q.append((row, col))
                        visited.add((row, col))
            return size

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and grid[i][j] not in visited:
                    res = max(res, bfs(i, j))

        return res
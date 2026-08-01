class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            grid[r][c] = 0 # instead of visited set
            q = deque([(r, c)])
            while q:
                row, col = q.popleft() # use pop to make it dfs
                neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                for n_r, n_c in neighbors:
                    if (n_r in range(rows) and
                    n_c in range(cols) and
                    grid[n_r][n_c] == "1"):
                        grid[n_r][n_c] = 0 # instead of visited set
                        q.append((n_r, n_c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)

        return islands


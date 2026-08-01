class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minutes = 0

        fresh_count = 0
        new_rotten = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    new_rotten.append((i, j))
        if fresh_count == 0:
            return 0
        if not new_rotten:
            return -1

        while new_rotten and fresh_count > 0:
            impacted = False
            for _ in range(len(new_rotten)):
                r, c = new_rotten.popleft()
                neighbors = [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]
                for row, col in neighbors:
                    if (row in range(rows) and 
                    col in range(cols) and
                    grid[row][col] == 1):
                        new_rotten.append((row, col))
                        grid[row][col] = 2
                        fresh_count -= 1
                        impacted = True
            if not impacted:
                return -1
            minutes += 1

        return minutes
        
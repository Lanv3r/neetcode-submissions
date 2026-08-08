class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        adj = {}
        for i in range(ROWS):
            for j in range(COLS):
                adj[(i, j)] = []
                if i > 0:
                    if grid[i][j] - grid[i-1][j] >= 0:
                        dist = 0
                    else:
                        dist = grid[i-1][j] - grid[i][j]
                    adj[(i, j)].append((dist, (i - 1, j)))
                if j > 0:
                    if grid[i][j] - grid[i][j-1] >= 0:
                        dist = 0
                    else:
                        dist = grid[i][j-1] - grid[i][j]
                    adj[(i, j)].append((dist, (i, j - 1)))
                if i < ROWS - 1:
                    if grid[i][j] - grid[i+1][j] >= 0:
                        dist = 0
                    else:
                        dist = grid[i+1][j] - grid[i][j]
                    adj[(i, j)].append((dist, (i + 1, j)))
                if j < COLS - 1:
                    if grid[i][j] - grid[i][j+1] >= 0:
                        dist = 0
                    else:
                        dist = grid[i][j+1] - grid[i][j]
                    adj[(i, j)].append((dist, (i, j + 1)))

        shortest = {}
        minheap = [(grid[0][0], (0, 0))]
        while minheap:
            t1, coor = heapq.heappop(minheap)
            i, j = coor
            if coor in shortest:
                continue
            shortest[coor] = t1
            if coor == (ROWS - 1, COLS - 1):
                for coor, time in shortest.items():
                    print(coor, time)
                return t1

            if i > 0:
                if t1 >= grid[i-1][j]:
                    heapq.heappush(minheap, (t1, (i-1, j)))
                else:
                    heapq.heappush(minheap, (grid[i-1][j], (i-1, j)))
            if j > 0:
                if t1 >= grid[i][j-1]:
                    heapq.heappush(minheap, (t1, (i, j-1)))
                else:
                    heapq.heappush(minheap, (grid[i][j-1], (i, j-1)))      
            if i < ROWS - 1:
                if t1 >= grid[i+1][j]:
                    heapq.heappush(minheap, (t1, (i+1, j)))
                else:
                    heapq.heappush(minheap, (grid[i+1][j], (i+1, j)))
            if j < COLS - 1:
                if t1 >= grid[i][j+1]:
                    heapq.heappush(minheap, (t1, (i, j+1)))
                else:
                    heapq.heappush(minheap, (grid[i][j+1], (i, j+1)))



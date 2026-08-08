class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        shortest = {}
        minheap = [(grid[0][0], (0, 0))]
        while minheap:
            t1, coor = heapq.heappop(minheap)
            i, j = coor
            if coor in shortest:
                continue
            shortest[coor] = t1
            if coor == (ROWS - 1, COLS - 1):
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



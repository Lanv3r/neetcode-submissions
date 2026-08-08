class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        visited = set()
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        while len(visited) < n:
            next_val, next_i = float('inf'), -1
            for i in range(n):
                if i not in visited and min_dist[i] < next_val:
                    next_val = min_dist[i]
                    next_i = i
            visited.add(next_i)
            res += next_val
            for i in range(n):
                if i not in visited:
                    min_dist[i] = min(min_dist[i], abs(points[next_i][0] - points[i][0]) + abs(points[next_i][1] - points[i][1]))
        return res

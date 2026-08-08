class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        visited = set()
        minheap = [(0, 0, 0)]
        while minheap:
            dist, src, tar = heapq.heappop(minheap)
            if tar in visited:
                continue
            visited.add(tar)
            res += dist
            for i in range(len(points)):
                if i not in visited:
                    dist = abs(points[tar][0] - points[i][0]) + abs(points[tar][1] - points[i][1])
                    heapq.heappush(minheap, (dist, tar, i))
        return res

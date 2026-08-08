class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((j, dist))
                adj[j].append((i, dist))
        minheap = []
        for neighbor, dist in adj[0]:
            heapq.heappush(minheap, (dist, 0, neighbor))
        visited = set()
        visited.add(0)
        while minheap:
            dist, src, tar = heapq.heappop(minheap)
            if tar in visited:
                continue
            visited.add(tar)
            res += dist
            for neighbor, dist in adj[tar]:
                if neighbor not in visited:
                    heapq.heappush(minheap, (dist, tar, neighbor))
        return res

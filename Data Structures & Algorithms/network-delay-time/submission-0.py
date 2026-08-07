class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        for src, tar, time in times:
            adj[src].append((tar, time))

        shortest = {}
        minheap = [(0, k)]
        res = 0
        while minheap:
            time, node = heapq.heappop(minheap)
            if node in shortest:
                continue
            shortest[node] = time
            res = max(res, time)
            for tar, t in adj[node]:
                if tar not in shortest:
                    heapq.heappush(minheap, (time + t, tar))
        if len(shortest) == n:
            return res
        else:
            return -1
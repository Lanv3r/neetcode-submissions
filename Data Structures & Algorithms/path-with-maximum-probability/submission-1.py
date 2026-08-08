class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            adj[a].append((succProb[i], b))
            adj[b].append((succProb[i], a))
        
        maxheap = [(1, start_node)]
        prob = {}
        while maxheap:
            p1, v1 = heapq.heappop_max(maxheap)
            if v1 in prob:
                continue
            prob[v1] = p1
            if v1 == end_node:
                return p1
            for p2, v2 in adj[v1]:
                if v2 not in prob:
                    heapq.heappush_max(maxheap, (p1*p2, v2))
        return 0


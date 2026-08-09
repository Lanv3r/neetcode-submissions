class UnionFind:
    def __init__(self, n):
        self.parent = {i : i for i in range(n)}
        self.rank = {i : 0 for i in range(n)}
    
    def find(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def get_mst_weight(n, sorted_edges, skip_idx=-1, force_idx=-1):
            uf = UnionFind(n)
            weight = 0
            edges_count = 0
            
            if force_idx != -1:
                a, b, w = edges[force_idx] # Note: use original edge data
                uf.union(a, b)
                weight += w
                edges_count += 1
                
            for w, a, b, idx in sorted_edges:
                if idx == skip_idx or idx == force_idx:
                    continue
                if uf.union(a, b):
                    weight += w
                    edges_count += 1
                    
            return weight if edges_count == n - 1 else float('inf')

        sorted_edges = []
        for i, (a, b, w) in enumerate(edges):
            sorted_edges.append((w, a, b, i))
        sorted_edges.sort(key=lambda x: x[0])

        mst_w = get_mst_weight(n, sorted_edges)

        critical = []
        pseudo = []
        for i in range(len(edges)):
            #exclude
            w1 = get_mst_weight(n, sorted_edges, skip_idx=i)
            if w1 > mst_w:
                critical.append(i)
                continue
            #include
            w2 = get_mst_weight(n, sorted_edges, force_idx=i)
            if w2 == mst_w:
                pseudo.append(i)
        return [critical, pseudo]

    



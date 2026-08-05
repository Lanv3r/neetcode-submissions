class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        p = self.parent[n]
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]      
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionFind = UnionFind(len(edges))
        for n1, n2 in edges:
            if not unionFind.union(n1, n2):
                return [n1, n2]


        
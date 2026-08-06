class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}

    def find(self, n1):
        p = self.parent[n1]
        while p != self.parent[p]:
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToInd = {}

        for i, a in enumerate(accounts):
            for e in accounts[i][1:]:
                if e in emailToInd:
                    uf.union(i, emailToInd[e])
                else:
                    emailToInd[e] = i
        
        emailGroup = defaultdict(list)
        for e, i in emailToInd.items():
            emailGroup[uf.find(i)].append(e)

        res = []
        for i, group in emailGroup.items():
            res.append([accounts[i][0]] + sorted(group))
        return res


        
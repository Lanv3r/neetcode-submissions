class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)

        visited = set()
        path = set()
        topSort = []
        for a in range(numCourses):
            if not self.dfs(a, adj, visited, path, topSort):
                return []
        return topSort

    def dfs(self, a, adj, visited, path, topSort):
        if a in path:
            print("in path")
            return False
        if a in visited:
            return True
        visited.add(a)
        path.add(a)
        for b in adj[a]:
            if not self.dfs(b, adj, visited, path, topSort):
                return False
        topSort.append(a)
        path.remove(a)
        return True
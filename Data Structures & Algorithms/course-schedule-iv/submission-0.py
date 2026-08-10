class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
          
        answer = []
        for b, a in queries:
            visited = set()
            answer.append(self.dfs(a, adj, visited, b))
        return answer

    def dfs(self, a, adj, visited, prereq):
        if a in visited:
            return False
        visited.add(a)
        for b in adj[a]:
            if b == prereq:
                return True
            if self.dfs(b, adj, visited, prereq):
                return True
        return False
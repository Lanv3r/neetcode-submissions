class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i:[] for i in range(numCourses)}
        
        for c, p in prerequisites:
            prereqs[c].append(p)
   
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if prereqs[course] == []:
                return True
            visited.add(course)
            for p in prereqs[course]:
                if not dfs(p):
                    return False
            prereqs[course] = []
            visited.remove(course)
            return True
        for c in prereqs:
            if not dfs(c):
                return False
        return True




        
            
        
        


        
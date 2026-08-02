class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_to_take = list(range(numCourses))
        prereqs = {}
        taken = set()
        
        for c, p in prerequisites:
            if c not in prereqs:
                prereqs[c] = []
            prereqs[c].append(p)
     
        while True:
            took_new_course = False
            if len(courses_to_take) == 0:
                return True
            for c in courses_to_take:
                if c not in prereqs or all(p in taken for p in prereqs[c]):
                    taken.add(c)
                    courses_to_take.remove(c)
                    took_new_course = True     
            if not took_new_course:
                return False


        
            
        
        


        
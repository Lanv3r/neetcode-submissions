class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int: 
        while True:
            took = False
            for i in range(len(students)):
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                    took = True
                    if len(students) == 0:
                        return 0
                else:
                    students.append(students.pop(0))
            if not took:
                return len(students)
            
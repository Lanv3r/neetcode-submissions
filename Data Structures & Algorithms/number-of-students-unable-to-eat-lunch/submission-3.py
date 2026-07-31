class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int: 
        n = len(students)
        st_freq = defaultdict(int)
        for s in students:
            st_freq[s] += 1
        
        for i in range(n):
            sandwich = sandwiches[i]
            if st_freq[sandwich] > 0:
                st_freq[sandwich] -= 1
            else:
                return n - i
        return 0
            
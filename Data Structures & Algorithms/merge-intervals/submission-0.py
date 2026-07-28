class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = []

        i = 0
        while i < n:
            k = i + 1
            cur_i = intervals[i]
            while k < n and intervals[i][1] >= intervals[k][0]:
                cur_i[1] = max(cur_i[1], intervals[k][1])
                k += 1
            res.append(cur_i)
            i = k

        return res


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        count = 0
        i = 1
        k = 0
        while i < n:
            if intervals[i][0] < intervals[k][1]:
                if intervals[i][1] > intervals[k][1]:
                    #intervals.pop(i)
                    pass
                else: 
                    #intervals.pop(k)
                    k = i
                count += 1
            else:
                k = i
            i += 1
        return count

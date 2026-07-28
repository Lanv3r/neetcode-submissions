class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        count = 0
        i = 1
        while i < n:
            if intervals[i][0] < intervals[i-1][1]:
                if intervals[i][1] > intervals[i-1][1]:
                    intervals.pop(i)
                else: 
                    intervals.pop(i-1)
                i -= 1
                n -= 1
                count += 1
            i += 1
        return count

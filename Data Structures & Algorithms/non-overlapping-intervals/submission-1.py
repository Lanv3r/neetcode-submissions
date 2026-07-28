class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        count = 0
        for i in range(1, n):
            k = i - 1
            while k >= 0:
                if intervals[k] != 0:
                    if intervals[i][0] < intervals[k][1]:
                        if intervals[i][1] > intervals[k][1]:
                            intervals[i] = 0
                        else: 
                            intervals[k] = 0
                        count += 1
                    break
                k -= 1
        return count

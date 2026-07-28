class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        new_s, new_e = s, e
        added = False
        res = []
        for i in range(len(intervals)):
            if intervals[i][1] < s:
                #before new interval
                res.append(intervals[i])
            elif intervals[i][0] > e:
                #after new interval
                if not added:
                    added = True
                    res.append([new_s, new_e])
                res.append(intervals[i])
            else:
                #overlap with new interval
                new_s = min(new_s, intervals[i][0])
                new_e = max(new_e, intervals[i][1])
        if not added:
            res.append([new_s, new_e])
        return res
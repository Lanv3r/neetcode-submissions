"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda x: x.start)
        res = 1
        rooms_ends = [intervals[0].end]
        for i in range(1, n):
            s, e = intervals[i].start, intervals[i].end
            #more than 1 room can free up but we don't care because we take at most 1 room per iteration
            if rooms_ends and s >= rooms_ends[0]:
                heapq.heappop(rooms_ends)
            heapq.heappush(rooms_ends, e)
            res = max(res, len(rooms_ends))       

        return res
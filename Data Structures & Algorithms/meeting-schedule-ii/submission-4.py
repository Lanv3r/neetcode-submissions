"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap = []
        for i in intervals:
            #more than 1 room can free up but we don't care because we take at most 1 room per iteration
            if heap and i.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)      
        #the length of the heap remains the maximum number of simultaneously occupied rooms
        return len(heap)
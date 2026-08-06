from sortedcontainers import SortedList
class MyCalendar:
    
    def __init__(self):
        self.events = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        ind = self.events.bisect_left((startTime, endTime))
        if ind > 0 and self.events[ind-1][1] > startTime:
            return False
        if ind < len(self.events) and self.events[ind][0] < endTime:
            return False
        self.events.add((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
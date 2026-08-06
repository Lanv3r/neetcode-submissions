class Node:
    def __init__(self, s, e):
        self.S = s
        self.E = e
        self.left, self.right = None, None       

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if self.root is None:
            self.root = Node(startTime, endTime)
            return True
        return self.helper(startTime, endTime)
    
    def helper(self, startTime, endTime):   
        cur = self.root
        while True:
            if endTime <= cur.S:
                if cur.left is None:
                    cur.left = Node(startTime, endTime)
                    return True
                cur = cur.left
            elif startTime >= cur.E:
                if cur.right is None:
                    cur.right = Node(startTime, endTime)
                    return True
                cur = cur.right
            else:
                return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
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
        return self.helper(self.root, startTime, endTime)
    
    def helper(self, node, startTime, endTime):   
        if not (endTime <= node.S or startTime >= node.E):
            return False

        if node.E <= startTime:
            if node.right is None:
                node.right = Node(startTime, endTime)
                return True
            else:
                return self.helper(node.right, startTime, endTime)
        else:
            if node.left is None:
                node.left = Node(startTime, endTime)
                return True
            else:
                return self.helper(node.left, startTime, endTime)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
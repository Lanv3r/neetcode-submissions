class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def getNode(self, index: int):
        if index < 0 or index >= self.length:
            return None
        i = 0
        curN = self.head
        while i < index:
            curN = curN.next
            i += 1
        return curN

    def get(self, index: int) -> int:
        node = self.getNode(index)
        if node is not None:
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val, self.head)
        self.head = new_head
        if self.tail is None:
            self.tail = self.head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_tail = ListNode(val, None)
        if self.tail is not None:
            self.tail.next = new_tail
        self.tail = new_tail
        if self.head is None:
            self.head = self.tail
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index == self.length:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        prevN = self.getNode(index - 1)
        nextN = prevN.next
        newN = ListNode(val, nextN)
        prevN.next = newN
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.length >= 1:
            if index == 0:
                self.head = self.hea.next
                self.length -=1
            elif index == self.length - 1:
                self.tail = self.getNode(index - 1)
                self.length -=1
            elif index > 0 and index < self.length - 1:
                prevN = self.getNode(index - 1)
                nextN = prevN.next.next
                prevN.next = nextN
                self.length -=1
               



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
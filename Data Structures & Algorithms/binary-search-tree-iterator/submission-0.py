# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []
        self.pointer = self.root  

    def next(self) -> int:
        while self.pointer is not None:
            self.stack.append(self.pointer)
            self.pointer = self.pointer.left   
        self.pointer = self.stack.pop()
        tmp = self.pointer.val
        self.pointer = self.pointer.right
        return tmp
    

    def hasNext(self) -> bool:
        if self.pointer or self.stack:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
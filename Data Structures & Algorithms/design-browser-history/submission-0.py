class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        n = len(self.stack) - self.pos - 1
        for i in range(n):
            self.stack.pop()
        self.stack.append(url)
        self.pos = len(self.stack) - 1

    def back(self, steps: int) -> str:
        while steps > 0 and self.pos > 0:
            self.pos -= 1
            steps -= 1
        return self.stack[self.pos]

    def forward(self, steps: int) -> str:
        n = len(self.stack)
        while steps > 0 and self.pos < n - 1:
            self.pos += 1
            steps -= 1
        return self.stack[self.pos]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
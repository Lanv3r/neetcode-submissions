class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.pos = 0
        self.n = 1

    def visit(self, url: str) -> None:
        if self.pos + 1 == self.n and self.n == len(self.stack):
            self.stack.append(url)
            self.n += 1
        else:
            self.stack[self.pos + 1] = url
            self.n = self.pos + 2
        self.pos = self.n - 1

    def back(self, steps: int) -> str:
        self.pos -= min(steps, self.pos)
        return self.stack[self.pos]

    def forward(self, steps: int) -> str:
        self.pos += min(steps, self.n - 1 - self.pos)
        return self.stack[self.pos]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
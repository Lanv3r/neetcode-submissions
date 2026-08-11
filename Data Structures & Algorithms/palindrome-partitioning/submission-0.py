class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        part = []

        def dfs(i):
            if i >= n:
                res.append(part.copy())
                return
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res


    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [1] * n
        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                cache[col] += cache[col + 1]
        return cache[0]
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        dp = [1] * (N + 1)
        for i in range(1, M + 1):
            cur = [0] * (N + 1)
            for j in range(1, N + 1):
                if t[i-1] == s[j-1]:
                    cur[j] = cur[j-1] + dp[j-1]
                else:
                    cur[j] = cur[j-1]
            dp = cur
        return dp[N]
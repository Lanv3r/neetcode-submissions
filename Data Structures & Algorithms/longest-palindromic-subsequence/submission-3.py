class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [0] * N
        for l in reversed(range(N)):
            cur = [-1] * N
            for r in range(N):
                if l > r:
                    cur[r] = 0
                elif l == r:
                    cur[r] = 1
                elif s[l] == s[r]:
                    cur[r] = 2 + dp[r-1]
                else:
                    cur[r] = max(cur[r - 1], dp[r])
            dp = cur
        return dp[N-1]
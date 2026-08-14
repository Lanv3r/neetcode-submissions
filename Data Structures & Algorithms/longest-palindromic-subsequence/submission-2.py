class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        res = 0
        cache = [[-1] * N for _ in range(N)]

        def dp(l, r):
            if l < 0 or r == N or l > r:
                return 0

            if cache[l][r] != -1:
                return cache[l][r]

            if l == r:
                cache[l][r] = 1
                return 1

            if s[l] == s[r]:
                cache[l][r] = 2 + dp(l + 1, r - 1)
            else:
                cache[l][r] = max(dp(l + 1, r), dp(l, r - 1))   
            return cache[l][r]

        dp(0, N - 1)
        return cache[0][N - 1]
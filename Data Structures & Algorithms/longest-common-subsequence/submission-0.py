class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        N, M = len(text1), len(text2)
        dp = [0] * (M + 1)
        for i in range(N):
            cur = [0] * (M + 1)
            for j in range(M):
                if text1[i] == text2[j]:
                    cur[j+1] = 1 + dp[j]
                else:
                    cur[j+1] = max(cur[j], dp[j+1])
            dp = cur
        return dp[M]
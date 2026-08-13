class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        dp = [_ for _ in range(M + 1)]
        print(dp)
        for i in range(1, N + 1):
            cur = [1] * (M + 1) 
            for j in range(1, M + 1):
                if word1[i-1] == word2[j-1]:
                    cur[j] = dp[j-1]
                else:
                    cur[j] = 1 + min(dp[j-1], dp[j], cur[j-1])
            dp = cur
            print(dp)

        return dp[M]
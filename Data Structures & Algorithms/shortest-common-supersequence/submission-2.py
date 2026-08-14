class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N, M = len(str1), len(str2)
        dp = [""] * (M + 1)
        for i in range(N, -1, -1):
            cur = [""] * (M + 1)
            for j in range(M, -1, -1):
                if i == N and j == M:
                    continue
                if i == N:
                    cur[j] = str2[j:]
                elif j == M:
                    cur[j] = str1[i:]
                else:
                    if str1[i] == str2[j]:
                        cur[j] = str1[i] + dp[j+1]
                    else:
                        if len(dp[j]) < len(cur[j+1]):
                            cur[j] = str1[i] + dp[j]
                        else:
                            cur[j] = str2[j] + cur[j+1]
            dp = cur
        return dp[0]
        

        
            
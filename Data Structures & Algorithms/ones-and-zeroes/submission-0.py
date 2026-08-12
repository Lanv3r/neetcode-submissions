class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(len(strs)):
            counts = Counter(strs[i])
            w0, w1 = counts.get('0', 0), counts.get('1', 0)
            for j in range(m, w0 - 1, -1):
                for k in range(n, w1 - 1, -1):
                    skip = dp[j][k]
                    include = 0
                    if j - w0 >= 0 and k - w1 >= 0:
                        include = 1 + dp[j - w0][k - w1] 
                    dp[j][k] = max(skip, include)
        return dp[m][n]

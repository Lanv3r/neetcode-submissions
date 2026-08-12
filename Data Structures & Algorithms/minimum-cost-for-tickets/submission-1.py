class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        start, end = days[0],days[-1]
        days_set = set(days)
        dp = [0] * (end - start + 2)
        for day in range(start, end + 1):
            ind = day - start + 1
            if day in days_set:
                dp[ind] = dp[ind-1] + costs[0]
                if day - 7 >= start:
                    dp[ind] = min(dp[ind], dp[ind-7] + costs[1])
                else:
                    dp[ind] = min(dp[ind], dp[0] + costs[1])
                if day - 30 >= start:
                    dp[ind] = min(dp[ind], dp[ind-30] + costs[2])
                else:
                    dp[ind] = min(dp[ind], dp[0] + costs[2])
            else: 
                dp[ind] = dp[ind-1]
        return dp[-1]
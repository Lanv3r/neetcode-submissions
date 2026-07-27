class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        cache = {}
        def dp(i, s):
            if i == len(nums):
                if s == target:
                    return 1
                return 0
            if (i, s) in cache:
                return cache[(i, s)]
            cache[(i, s)] = dp(i+1, s + nums[i]) + dp(i+1, s - nums[i])
            return cache[(i, s)]
        return dp(0, 0)


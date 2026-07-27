class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = [0] * len(nums)
        def dp(i, s):
            if i == len(nums):
                if s == target:
                    return 1
                return 0
            cache[i] = dp(i+1, s + nums[i]) + dp(i+1, s - nums[i])
            return cache[i]
        return dp(0, 0)


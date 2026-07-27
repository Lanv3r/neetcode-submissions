class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        prevCache = {0 : 1}
        for i in range(len(nums) - 1, -1, -1):
            curCache = {}
            for s, w in prevCache.items():
                curCache[s + nums[i]] = curCache.get(s + nums[i], 0) + w
                curCache[s - nums[i]] = curCache.get(s - nums[i], 0) + w
            prevCache = curCache
        return prevCache.get(target, 0)


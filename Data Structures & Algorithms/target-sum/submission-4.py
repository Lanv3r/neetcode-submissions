class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prevCache = defaultdict(int)
        prevCache[0] = 1
        for i in range(len(nums) - 1, -1, -1):
            curCache = defaultdict(int)
            for s, w in prevCache.items():
                curCache[s + nums[i]] += w
                curCache[s - nums[i]] += w
            prevCache = curCache
        return prevCache[target]


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, curMin = 0, 0
        globalMax, globalMin = nums[0], nums[0]
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            curMax = max(curMax + nums[i], nums[i])
            globalMax = max(globalMax, curMax)
            curMin = min(curMin + nums[i], nums[i])
            globalMin = min(globalMin, curMin)
        if total == globalMin:
            return globalMax
        else: 
            return max(globalMax, total - globalMin)
            
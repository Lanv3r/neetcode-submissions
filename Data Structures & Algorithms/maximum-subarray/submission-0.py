class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        prev = float('-inf')
        for i in range(len(nums)):
            prev = max(prev + nums[i], nums[i])
            res = max(res, prev)
        return res
            
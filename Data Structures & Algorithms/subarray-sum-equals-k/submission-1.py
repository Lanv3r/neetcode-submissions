class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sums = defaultdict(int)
        sums[0] = 1
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            res += sums[total - k]
            sums[total] += 1
        return res
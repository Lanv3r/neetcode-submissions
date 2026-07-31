class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for n in nums:
            if n == 1:
                cur += 1
            else:
                cur = 0
            res = max(res, cur)
        return res
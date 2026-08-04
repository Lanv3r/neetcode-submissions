class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        c = 0
        while r < len(nums):
            if nums[r] != nums[l]:
                nums[l+1] = nums[r]
                l += 1
                r += 1
                c = 0
            elif nums[r] == nums[l] and c == 0:
                nums[l+1] = nums[r]
                l += 1
                r += 1
                c = 1
            else:
                r += 1
        return l + 1
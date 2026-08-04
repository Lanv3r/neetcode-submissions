class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        l = 0
        prev_diff = None
        r = 1
        while r < len(arr):
            new_diff = arr[r] - arr[r-1]
            if new_diff == 0:
                l = r
                prev_diff = None
            elif prev_diff is None:
                prev_diff = new_diff
                res = max(res, r - l + 1)
            elif new_diff * prev_diff > 0:
                prev_diff = new_diff
                l = r - 1
            else:
                prev_diff = new_diff
                res = max(res, r - l + 1)
            r += 1
        return res
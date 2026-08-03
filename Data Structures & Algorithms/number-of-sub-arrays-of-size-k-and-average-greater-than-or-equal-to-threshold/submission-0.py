class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        window_sum = 0
        l = 0
        for r in range(len(arr)):
            if r - l + 1 > k:
                window_sum -= arr[l]
                l += 1
            window_sum += arr[r]
            if r - l + 1 == k and (window_sum / k) >= threshold:
                res += 1
        return res
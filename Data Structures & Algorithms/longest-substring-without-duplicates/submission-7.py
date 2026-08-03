class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        window = set()
        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, r - l + 1)
        return res
        
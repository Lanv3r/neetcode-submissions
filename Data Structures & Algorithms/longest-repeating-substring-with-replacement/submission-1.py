class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            max_f = 0
            for let, f in count.items():
                max_f = max(max_f, f)
            while r - l + 1 - max_f > k:
                count[s[l]] -= 1
                l += 1
                for let, f in count.items():
                    max_f = max(max_f, f)
            res = max(res, r - l + 1)
        return res
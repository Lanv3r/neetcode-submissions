class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        res = s
        answer = False

        counts = Counter(t)
        letters = len(counts)
        l, r = 0, 0
        while r < len(s) and l < len(s):
            if letters > 0:
                if s[r] in counts:
                    counts[s[r]] -= 1
                    if counts[s[r]] == 0:
                        letters -= 1
                r += 1
            else:
                answer = True
                if r - l < len(res):
                    res = s[l:r]
                if s[l] in counts:
                    counts[s[l]] += 1
                    if counts[s[l]] == 1:
                        letters = 1
                l += 1
        while letters == 0 and l < len(s):
            answer = True
            if r - l < len(res):
                res = s[l:r]
            if s[l] in t:
                counts[s[l]] += 1
                if counts[s[l]] == 1:
                    letters = 1
            l += 1

        if not answer:
            return ""
        return res
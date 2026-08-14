class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0

        for i in range(N):
            #odd length
            l, r = i, i
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

            #even length
            l, r = i, i + 1
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

        return res
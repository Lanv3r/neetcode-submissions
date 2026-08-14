class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(s1, s2, s3, i, j, k, cache):
            if k == len(s3) and i == len(s1) and j == len(s2):
                return True

            if (i, j, k) in cache:
                return cache[(i, j, k)]

            cache[(i, j, k)] = False
            if i < len(s1) and s1[i] == s3[k]:
                cache[(i, j, k)] = cache[(i, j, k)] or dfs(s1, s2, s3, i+1, j, k+1, cache)
            if j < len(s2) and s2[j] == s3[k]:  
                cache[(i, j, k)] = cache[(i, j, k)] or dfs(s1, s2, s3, i, j+1, k+1, cache)
            return cache[(i, j, k)]

        if len(s1) + len(s2) != len(s3):
            return False

        return dfs(s1, s2, s3, 0, 0, 0, {})
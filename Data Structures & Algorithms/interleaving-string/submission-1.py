class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(s1, s2, s3, i, j, cache):
            if i == len(s1) and j == len(s2):
                return True

            if (i, j) in cache:
                return cache[(i, j)]

            cache[(i, j)] = False
            if i < len(s1) and s1[i] == s3[i+j]:
                cache[(i, j)] = cache[(i, j)] or dfs(s1, s2, s3, i+1, j, cache)
            if j < len(s2) and s2[j] == s3[i+j]:  
                cache[(i, j)] = cache[(i, j)] or dfs(s1, s2, s3, i, j+1, cache)
            return cache[(i, j)]

        if len(s1) + len(s2) != len(s3):
            return False

        return dfs(s1, s2, s3, 0, 0, {})
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        cache = [[-1] * M for _ in range(N)] 
        def dfs(w1, w2, i, j, cache):
            if i >= N or j >= M:
                return max(N - i, M - j)
            if cache[i][j] != -1:
                return cache[i][j]
            
            if w1[i] == w2[j]:
                cache[i][j] = dfs(w1, w2, i + 1, j + 1, cache)
            else:
                cache[i][j] = 1 + min(
                    dfs(w1, w2, i + 1, j + 1, cache), 
                    dfs(w1, w2, i + 1, j, cache), 
                    dfs(w1, w2, i, j + 1, cache)
                ) 
            return cache[i][j]

        return dfs(word1, word2, 0, 0, cache)
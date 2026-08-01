class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        r, c = len(image), len(image[0])
        def dfs(i, j, visited):
            if i < 0 or i >= r:
                return
            if j < 0 or j >= c:
                return  
            if (i, j) in visited:
                return
            visited.add((i, j))
            if image[i][j] == original_color:
                image[i][j] = color
                dfs(i - 1, j, visited)
                dfs(i + 1, j, visited)
                dfs(i, j - 1, visited)
                dfs(i, j + 1, visited)

        dfs(sr, sc, set())
        return image
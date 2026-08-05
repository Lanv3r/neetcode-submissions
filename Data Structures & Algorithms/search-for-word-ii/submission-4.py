class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True 
        cur.index = index


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        res = []

        for i in range(len(words)):
            trie.insert(words[i], i) 

        def dfs(r, c, visited, root):
            if (
                r in range(ROWS) and 
                c in range(COLS) and 
                (r, c) not in visited 
                and board[r][c] in root.children
            ):
                visited.add((r, c))
                if r == 2 and c == 2:
                    print(visited)
                cur = root.children[board[r][c]]
                if cur.word and cur.index >= 0:
                    res.append(words[cur.index])
                    cur.index = -1
                dfs(r-1, c, visited, cur)
                dfs(r+1, c, visited, cur)
                dfs(r, c+1, visited, cur)
                dfs(r, c-1, visited, cur) 
                visited.remove((r, c))
                if len(cur.children) == 0 and cur.index < 0:
                    del root.children[board[r][c]]

        ROWS, COLS = len(board), len(board[0])
        cur = trie.root
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, visited, cur)

        return res
                



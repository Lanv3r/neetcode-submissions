import itertools
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word 


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        res = []
        board_counts = Counter(itertools.chain.from_iterable(board))
        words = [w for w in words if all(w.count(c) <= board_counts[c] for c in set(w))]

        for w in words:
            trie.insert(w) 

        def dfs(r, c, root):
            if (
                r in range(ROWS) and 
                c in range(COLS) and 
                board[r][c] != '#'
                and board[r][c] in root.children
            ):
                char = board[r][c]
                board[r][c] = '#' #save memory by not using sets
                cur = root.children[char]
                if cur.word is not None:
                    res.append(cur.word)
                    cur.word = None
                dfs(r-1, c, cur)
                dfs(r+1, c, cur)
                dfs(r, c+1, cur)
                dfs(r, c-1, cur) 
                board[r][c] = char #save memory by not using sets
                if not cur.children:
                    root.children.pop(char) #cleanup trie if the word was found
                
        
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root)

        return res
                



class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            if i == len(word):
                return root.word
            c = word[i]
            if c == ".":    
                for child in root.children:
                    if dfs(i+1, root.children[child]):
                        return True
                return False                  
            elif c not in root.children:
                return False
            return dfs(i+1, root.children[c])

        return dfs(0, self.root)

    





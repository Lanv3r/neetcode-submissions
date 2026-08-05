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
        roots = [self.root]
        k = 0
        while k < len(word):
            c = word[k]
            if c == ".":
                for r in roots:
                    new_roots = []
                    for child in r.children:
                        new_roots.append(r.children[child])                      
            else:
                new_roots = []
                for r in roots:
                    if c in r.children:
                        new_roots.append(r.children[c])
            roots = new_roots
            if not roots:
                return False
            k += 1
        for r in roots:
            if r.word:
                return True
        return False


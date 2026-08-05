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
        return self.helper(self.root, word, 0)

    def helper(self, root, word, i):
        cur = root
        k = i
        while k < len(word):
            c = word[k]
            if c == ".":
                for child in cur.children:
                    new_root = cur.children[child]
                    if self.helper(new_root, word, k + 1):
                        return True
                return False
            elif c not in cur.children:
                return False
            else:
                cur = cur.children[c]
            k += 1
        return cur.word
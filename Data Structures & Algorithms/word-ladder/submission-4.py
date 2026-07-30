import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        m = len(beginWord)
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        visited = set([beginWord])
        q = deque([(beginWord, 1)])
        letters = list(string.ascii_lowercase)
        
        while q:
            w, d = q.popleft()
            if w == endWord:
                return d
            
            for i in range(m):
                for l in letters:
                    new_word = w[:i]+l+w[i+1:]
                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        q.append((new_word, d + 1))
        return 0
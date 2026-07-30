class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        visited = set([beginWord])
        q = deque([(beginWord, 1)])
        
        while q:
            w, d = q.popleft()
            if w == endWord:
                return d
            for cand in wordList:
                if cand not in visited:
                    diffs = 0
                    for i in range(len(cand)):
                        if cand[i] != w[i]:
                            diffs += 1
                        if diffs > 1:
                            break
                    if diffs == 1:
                        visited.add(cand)
                        q.append((cand, d + 1))
        return 0
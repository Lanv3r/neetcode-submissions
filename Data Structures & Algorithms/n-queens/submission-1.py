class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        q_pos = set()

        def dfs(row):
            if len(q_pos) == n:
                board = []
                for i in range(n):
                    s = ""
                    for j in range(n):
                        if (i, j) in q_pos:
                            s += 'Q'
                        else:
                            s += '.'
                    board.append(s)
                res.append(board)
                return
            if row > n:
                return
            for col in range(n):
                pos2 = (row, col)
                allowed = True
                for pos1 in q_pos:
                    if self.canAttack(pos1, pos2):
                        allowed = False
                        break
                if allowed:
                    q_pos.add(pos2)
                    dfs(row + 1)
                    q_pos.remove(pos2)

        dfs(0)
        return res

    def canAttack(self, pos1, pos2):
        r1, c1 = pos1
        r2, c2 = pos2
        if r1 == r2:
            return True
        if c1 == c2:
            return True
        if (r1 - c1) == (r2 - c2):
            return True
        if (r1 + c1) == (r2 + c2):
            return True
        return False
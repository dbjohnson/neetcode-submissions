class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board[0])
        rows = board
        cols = [
            [row[col] for row in rows]
            for col in range(n)
        ]
        subs = [
            [
                board[ii][jj] 
                for ii in range(i, i + 3)
                for jj in range(j, j + 3)
            ]
            for i in range(0, len(rows), 3)
            for j in range(0, len(cols), 3)
            if max(i, j) < n
        ]
        return all([
            len(x) == len(set(x))
            for t in rows + cols + subs
            for x in [[c for c in t if c != '.']]
        ])
        
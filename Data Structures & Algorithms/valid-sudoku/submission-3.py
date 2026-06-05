class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows  = [0] * 9 
        cols = [0] * 9 
        squares = [0] * 9 
        for r in range(9):
            for c in range(9):
                if (board[r][c] == "."):
                    continue
                binval = int(board[r][c]) - 1
                if 1<<binval & rows[r]: return False
                if 1<<binval & cols[c]: return False
                if 1<<binval & squares[(r//3)  * 3 + (c//3)]: return False
                rows[r] |= ( 1 << binval)
                cols[c] |= ( 1 << binval)
                squares[(r//3)  * 3 + (c//3)] |= (1 << binval)
        return True
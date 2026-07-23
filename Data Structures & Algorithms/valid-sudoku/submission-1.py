class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                elif board[i][j] not in seen:
                    seen.add(board[i][j])
                elif board[i][j] in seen:
                    return False
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i]==".":
                    continue
                elif board[j][i] not in seen:
                    seen.add(board[j][i])
                elif board[j][i] in seen:
                    return False

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row=(square//3) *3 +i
                    col=(square%3) * 3+j
                    if board[row][col]==".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
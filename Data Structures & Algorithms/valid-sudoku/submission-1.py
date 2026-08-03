class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for val in row:
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)

        # columns
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] != ".":
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])

        # boxes
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                seen = set()
                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):
                        if board[r][c] != ".":
                            if board[r][c] in seen:
                                return False
                            seen.add(board[r][c])

        return True
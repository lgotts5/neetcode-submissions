class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(board,word,x,y):
            if len(word) == 0:
                return True
            if(x >= len(board) or x < 0 or y >= len(board[0]) or y < 0):
                return False
            if board[x][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = "8"
                res = backtrack(board,word[1:],x+1,y) or backtrack(board,word[1:],x-1,y) or backtrack(board,word[1:],x,y+1) or backtrack(board,word[1:],x,y-1)
                board[x][y] = tmp
                return res
            return False

        for i in range(len(board)):             
            for j in range(len(board[0])):                                                                                                                                   
                if backtrack(board, word, i, j):                                                                                                                             
                    return True                                                                                                                                              
        return False
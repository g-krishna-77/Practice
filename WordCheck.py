def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def backtrack(r, c, suffix):
        if len(suffix) == 0:  
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != suffix[0]:
            return False
        
        temp, board[r][c] = board[r][c], '#'
        
        res = (backtrack(r+1, c, suffix[1:]) or
               backtrack(r-1, c, suffix[1:]) or
               backtrack(r, c+1, suffix[1:]) or
               backtrack(r, c-1, suffix[1:]))
      
        board[r][c] = temp
        return res
    
    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, word):
                return True
    return False


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word1 = "ABCCED"
word2 = "ABCB"

print(exist(board, word1))  
print(exist(board, word2))  

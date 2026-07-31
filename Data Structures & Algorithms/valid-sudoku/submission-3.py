class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if board[r][c] in rows[r]:
                    return False
                else:
                    rows[r].add(board[r][c])
        
        for c in range(9):
            for r in range(9):
                if board[r][c]=='.':
                    continue
                if board[r][c] in cols[c]:
                    return False
                else:
                    cols[c].add(board[r][c])         
        
        for s in range(9):
            for i in range(3):
                for j in range(3):
                    row = (s//3)*3 +i 
                    column = (s%3)*3 + j
                    
                    if board[row][column] == '.':
                        continue
                    if board[row][column] in squares[s]:
                        return False
                    squares[s].add(board[row][column])

        return True

        
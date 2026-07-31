class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for r in range(9):
            seen= set()
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])
        
        for c in range(9):
            seen= set()
            for r in range(9):
                if board[r][c]=='.':
                    continue
                if board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])         
        
        for s in range(9):
            seen= set()
            for i in range(3):
                for j in range(3):
                    row = (s//3)*3 +i 
                    column = (s%3)*3 + j
                    
                    if board[row][column] == '.':
                        continue
                    if board[row][column] in seen:
                        return False
                    seen.add(board[row][column])

        return True

        
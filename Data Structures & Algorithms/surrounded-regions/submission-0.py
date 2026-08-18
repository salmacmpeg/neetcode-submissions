class Solution:
    def solve(self, board: List[List[str]]) -> None:
        all_b_o = []
        rows = len(board)
        cols = len(board[0])
        direction= [(1,0),(-1,0), (0,1),(0,-1)]
        for r in [0,rows-1]:
            for c in range(cols):
                if board[r][c] == "O":
                    all_b_o.append((r,c))
        for c in [0,cols-1]:
            for r in range(1,rows-1):
                if board[r][c] == "O":
                    all_b_o.append((r,c))
        # print("all_b_o",all_b_o)
        access = [[False]*cols for _ in range(rows)]
        for bi,bj in all_b_o:
           queue = deque([(bi,bj)])
           while len(queue)>0:
            nodei, nodej = queue.popleft()
            for dr,dc in direction:
                nr = nodei+dr
                nc = nodej+dc
                access[nodei][nodej] = True
                if nr>=0 and nr<rows and nc>=0 and nc<cols and board[nr][nc] !="X" and not access[nr][nc]:
                    queue.append((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and not access[r][c]:
                    board[r][c] = "X"


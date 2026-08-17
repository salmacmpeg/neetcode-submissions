class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        INF =2147483647
        visited = [[False]*COLS for _ in range(ROWS)]
        queue = deque([])

        for i in range(0,ROWS):
            for j in range(0,COLS):
                # print("grid[i][j]",grid[i][j])
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited[i][j] = True

        steps = 1   
        while len(queue)>0:
            # print(f"with steps = {steps} the queue has {queue}")
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in direction:
                    if r+dr>=0 and r+dr< ROWS and c+dc>=0 and c+dc< COLS and not visited[r+dr][c+dc] and grid[r+dr][c+dc]!=-1:
                        grid[r+dr][c+dc] = steps
                        queue.append((r+dr, c+dc)) 
                        visited[r+dr][c+dc]=True
            steps+=1

        




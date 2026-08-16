class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        def rec_dfs(r, c):
            if r<0 or c<0 or r>=ROWS or c >=COLS or grid[r][c]=="0":
                return
            
            grid[r][c] = "0"
            for dr,dc in direction:
                # print("dr", dr, "dc",dc)
                rec_dfs(r+dr,c+dc)
            return
        
        ROWS = len(grid)
        COLS = len(grid[0])
        # print("ROWS",ROWS,"COLS",COLS )
        num_islands = 0 
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    num_islands +=1
                    rec_dfs(i,j)
        return num_islands
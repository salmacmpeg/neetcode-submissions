class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
       
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        def rec_dfs(r, c):
            if r<0 or c<0 or r>=ROWS or c >=COLS or grid[r][c]==0:
                return 0 
            
            grid[r][c] = 0
            tsum= 1
            # print(f'tsum before for r{r},c{c} = tsum')
            for dr,dc in direction:
                # print("dr", dr, "dc",dc)
                tsum += rec_dfs(r+dr,c+dc)
            # print(f'tsum after for r{r},c{c} = tsum')
            return tsum
        
        ROWS = len(grid)
        COLS = len(grid[0])
        # print("ROWS",ROWS,"COLS",COLS )
        max_num = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    num_islands = 0
                    num_islands+= rec_dfs(i,j)
                    max_num = max(max_num,num_islands)
        return max_num
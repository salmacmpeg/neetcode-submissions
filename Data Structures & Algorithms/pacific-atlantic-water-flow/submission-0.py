class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        pacific = [[0]*cols  for r in range(rows)]
        atlantic = [[0]*cols  for r in range(rows)]
        #0 means not visited
        #1 visited but not reached from pacific ocean
        #2 visited and reached from the pacific ocean
        # return indiced of node where both pacific and atalantic =2

        #propagate the pacific 
        qpacific = deque([])
        qatla = deque([])

        for r in range(rows):
            for c in range(cols):
                if r==0:
                    qpacific.append((r,c))
                    pacific[r][c] = 2
                if r==rows-1:
                    qatla.append((r,c))
                    atlantic[r][c] = 2
                if r>0 and r<=rows-1 and c==0:
                    qpacific.append((r,c))
                    pacific[r][c] = 2
                if r>=0 and r<rows-1 and c==cols-1:
                    qatla.append((r,c))
                    atlantic[r][c] = 2
        
        while len(qpacific)>0:
            r,c = qpacific.popleft()
            for dr,dc in direction:
                nr= dr+r
                nc= dc+c
                if (nr>=0 and nr<rows and nc>=0 and nc<cols
                    and pacific[nr][nc]<2 
                    and heights[nr][nc]>= heights[r][c]):
                    pacific[nr][nc] =2
                    qpacific.append((nr,nc))
        while len(qatla)>0:
            r,c = qatla.popleft()
            for dr,dc in direction:
                nr= dr+r
                nc= dc+c
                if (nr>=0 and nr<rows and nc>=0 and nc<cols
                    and atlantic[nr][nc]<2 
                    and heights[nr][nc]>= heights[r][c]):
                    atlantic[nr][nc] =2
                    qatla.append((nr,nc))

        # print("heights",heights)
        # print("qpacific",qpacific)
        # print("qatla",qatla)
        # print("pacific",pacific)
        # print("atlantic",atlantic)

        res =[]
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] == atlantic[r][c] == 2:
                    res.append([r,c])

        return res

        

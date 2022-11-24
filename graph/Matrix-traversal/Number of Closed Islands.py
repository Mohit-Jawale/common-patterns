class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROW,COL = len(grid),len(grid[0])

        number_of_closed_island = 0
        corner_alert = False
        def dfs(r,c):
            nonlocal corner_alert
            if grid[r][c]==0:
                if r==0 or r==ROW-1 or c==0 or c==COL-1:
                    corner_alert = True
                grid[r][c]=2
                if r>=1:dfs(r-1,c)
                if r+1<ROW:dfs(r+1,c)
                if c>=1:dfs(r,c-1)
                if c+1<COL:dfs(r,c+1)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==0 and grid[i][j]!=2:
                    dfs(i,j)
                    if corner_alert== False:
                        number_of_closed_island+=1
                    corner_alert = False

        return(number_of_closed_island)








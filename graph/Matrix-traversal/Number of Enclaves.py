class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid),len(grid[0])
        number_of_land_cells = 0
        boundary_cell_alert = False
        area = 0


        def dfs(r,c):
            nonlocal boundary_cell_alert
            nonlocal area
            if grid[r][c]==1:
                if r==0 or r == ROW-1 or c==0 or c==COL-1:
                    boundary_cell_alert=True
                area+=1    
                grid[r][c]=2
                if r>=1:dfs(r-1,c)
                if r+1<ROW:dfs(r+1,c)
                if c>=1:dfs(r,c-1)
                if c+1<COL:dfs(r,c+1)

        ans = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==1 and grid[i][j]!=2:
                    dfs(i,j)
                    if not boundary_cell_alert :
                        ans+=area
                    area=0
                    boundary_cell_alert = False


        return ans

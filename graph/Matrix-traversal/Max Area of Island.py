class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW,COL = len(grid), len(grid[0])

        area = 0
        max_area = 0
        number_of_island = 0

        def dfs(r,c):
            nonlocal area
            if grid[r][c]==1:
                grid[r][c]=2
                area+=1
                if r>=1:dfs(r-1,c)
                if r+1<ROW:dfs(r+1,c)
                if c>=1:dfs(r,c-1)
                if c+1<COL:dfs(r,c+1)

        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==1 and grid[i][j]!=2:
                    dfs(i,j)
                    number_of_island+=1
                    max_area = max(max_area,area)
                    area=0

        return max_area      

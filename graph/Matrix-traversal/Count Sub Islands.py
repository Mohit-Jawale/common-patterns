class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        R , C = len(grid1),len(grid2[0])
        number_of_subisland = 0
        not_subisland = True
        def dfs(r,c):
            if grid1[r][c]==grid2[r][c] and grid1[r][c]==1:
                grid1[r][c]=2
                grid2[r][c]=2
                if r>=1:dfs(r-1,c)
                if r+1<R:dfs(r+1,c)
                if c>=1:dfs(r,c-1)
                if c+1<C:dfs(r,c+1)

        def dfs_find_island(r,c):
            nonlocal not_subisland
            if grid2[r][c]==2 or grid2[r][c]==1:
                if grid2[r][c]==1:
                    not_subisland = False
                grid2[r][c]=3    
                if r>=1:dfs_find_island(r-1,c)
                if r+1<R:dfs_find_island(r+1,c)
                if c>=1:dfs_find_island(r,c-1)
                if c+1<C:dfs_find_island(r,c+1)

                     

        for i in range(R):
            for j in range(C):
                if grid1[i][j]==1 and grid1[i][j]!=2:
                    dfs(i,j)

        for i in range(R):
            for j in range(C):
                if (grid2[i][j]==2 or  grid2[i][j]==1) and grid2[i][j]!=3:
                    dfs_find_island(i,j)
                    if not_subisland:
                        number_of_subisland+=1
                    not_subisland = True
                 
        return(number_of_subisland)            



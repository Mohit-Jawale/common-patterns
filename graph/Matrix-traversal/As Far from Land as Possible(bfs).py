class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid),len(grid[0])

        all_ones = set()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==1:
                    all_ones.add((i,j))

        itr = 0
        while all_ones:
            temp_set = set()
            itr+=1

            for ones in all_ones:
                r = ones[0]
                c= ones[1]

                #top cell
                if r!=0 and grid[r-1][c]==0:
                    grid[r-1][c]=1
                    temp_set.add((r-1,c))
                #bottom cell
                if r!=ROW-1 and grid[r+1][c]==0:
                    grid[r+1][c]=1
                    temp_set.add((r+1,c))
                #left cell
                if c!=0 and grid[r][c-1]==0:
                    grid[r][c-1]=1
                    temp_set.add((r,c-1))
                #right cell
                if c!=COL-1 and grid[r][c+1]==0:
                    grid[r][c+1]=1
                    temp_set.add((r,c+1))
            all_ones = temp_set

        if itr-1 == 0:
            return -1
        return itr-1        

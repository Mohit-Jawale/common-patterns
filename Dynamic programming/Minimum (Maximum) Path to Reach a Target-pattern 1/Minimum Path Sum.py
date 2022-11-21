class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        
        Matrix = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        

           
        for i in range(0,len(grid)):
            for j in range(len(grid[0])):
                if i==0:
                    Matrix[i][j]= Matrix[i][j-1] + grid[i][j]
                else:
                    if j ==0 :
                        up = Matrix[i-1][j] + grid[i][j]
                        Matrix[i][j] = up
                    else:
                        up = Matrix[i-1][j] + grid[i][j]
                        left = Matrix[i][j-1] + grid[i][j]
                        min_path = min(up,left)
                        Matrix[i][j] = min_path

        return Matrix[len(grid)-1][len(grid[0])-1]                

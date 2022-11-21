class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        ans = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]


        row = len(matrix)
        col = len(matrix[0])
        for i in range(0,row):
            for j in range(0,col):
                if i==0:
                    ans[i][j] = matrix[i][j] 
        
                else:
                    if j==0:
                        fall_min = min(ans[i-1][j]+matrix[i][j],ans[i-1][j+1]+matrix[i][j])
                        ans[i][j]=fall_min
                    elif j==col-1:
                        fall_min = min(ans[i-1][j]+matrix[i][j],ans[i-1][j-1]+matrix[i][j])
                        ans[i][j]=fall_min

                    else:
                        fall_min = min(ans[i-1][j]+matrix[i][j],ans[i-1][j+1]+matrix[i][j],ans[i-1][j-1]+matrix[i][j])
                        ans[i][j]=fall_min
        
        return(min(ans[row-1]))

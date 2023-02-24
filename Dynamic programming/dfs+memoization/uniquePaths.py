class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}

        def dfs(row,col):

            nonlocal memo

            if row == 0 or col == 0:
                return 1

            if (row,col) in memo:
                return memo[(row,col)]

            memo[(row,col)]=  dfs(row-1,col) + dfs(row,col-1)

            return memo[(row,col)]

        return dfs(m-1,n-1)
        

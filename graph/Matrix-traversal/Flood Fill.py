class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        R,C = len(image),len(image[0])
        newcolor = image[sr][sc]

        if newcolor == color:
            return image

        def dfs(r,c):

            if newcolor == image[r][c] :
                image[r][c] = color
                if r>=1: dfs(r-1,c)
                if r+1<R:dfs(r+1,c)
                if c>=1:dfs(r,c-1)
                if c+1<C:dfs(r,c+1)
                
        dfs(sr,sc)
        return image           
        

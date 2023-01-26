class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []
        row,col  = len(matrix), len(matrix[0])
        left,right = 0,col-1
        top, bottom = 0, row - 1

        while left<=right and top<=bottom:
            
            #### from left to right with top as constant row
            for i in range(left,right+1):
                ans.append(matrix[top][i])

            top+=1
            #### from top to bottom with right as constant col
            for j in range(top,bottom+1):
                ans.append(matrix[j][right])

            right-=1
            
            #### from right to left with bottom as constant row and remember the top to bottom condition here it is there to check if top has not crossed
            ##### the bottom yet if top is greater that means the row is already visited 
            if top<=bottom:
                for k in range(right,left-1,-1):
                    ans.append(matrix[bottom][k])
                bottom-=1    

          
             ### same here also
            if left<=right:
                for l in range(bottom,top-1,-1):
                    ans.append(matrix[l][left])
                left+=1    

                    

        return ans                    




   

    
